from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import mysql
import bcrypt

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        if not email or not password:
            flash("Email and password are required.", "danger")
            return redirect(url_for("auth.login"))

        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT user_id, full_name, password_hash FROM users WHERE email = %s",
                (email,),
            )
            user = cur.fetchone()
            cur.close()
        except Exception as e:
            flash(f"Database error: {e}", "danger")
            return redirect(url_for("auth.login"))

        if not user:
            flash("Invalid email or password.", "danger")
            return redirect(url_for("auth.login"))

        stored_hash = user[2]
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode("utf-8")

        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            # Set session
            session['user_id'] = user[0]
            session['full_name'] = user[1]
            session['email'] = email
            session['is_admin'] = False  # No is_admin column, default non-admin
            
            # Auto create account if not exists
            cur = mysql.connection.cursor()
            cur.execute("SELECT account_id FROM accounts WHERE user_id=%s", (user[0],))
            account = cur.fetchone()
            if not account:
                import random
                account_number = "SB" + str(random.randint(1000000000,9999999999))
                cur.execute(
                    "INSERT INTO accounts (user_id, account_number, balance, status) VALUES (%s,%s,%s,%s)",
                    (user[0], account_number, 0, "active")
                )
                mysql.connection.commit()
            cur.close()
            
            flash("Login successful!", "success")
            return redirect(url_for("dashboard.index"))

        flash("Invalid email or password.", "danger")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        password = request.form.get("password", "")

        if not full_name or not email or not password:
            flash("Name, email and password are required.", "danger")
            return redirect(url_for("auth.register"))

        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO users (full_name, email, phone, password_hash) "
                "VALUES (%s, %s, %s, %s)",
                (full_name, email, phone, hashed),
            )
            user_id = cur.lastrowid
            mysql.connection.commit()
            
            # Auto create account for new user
            import random
            account_number = ''.join(['%d' % random.randint(0, 9) for num in range(20)])
            cur.execute(
                "INSERT INTO accounts (user_id, account_number, balance) VALUES (%s, %s, 0.00)",
                (user_id, account_number)
            )
            mysql.connection.commit()
            cur.close()
            flash("Registration successful with account created. Please log in.", "success")
            return redirect(url_for("auth.login"))
        except Exception as e:
            flash(f"Registration failed: {e}", "danger")
            return redirect(url_for("auth.register"))

    return render_template("register.html")


@bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))

