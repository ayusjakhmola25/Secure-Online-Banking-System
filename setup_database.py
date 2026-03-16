import MySQLdb
import bcrypt

try:
    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='ayush123'
    )
    cursor = conn.cursor()
    
    # Create database
    cursor.execute('CREATE DATABASE IF NOT EXISTS securebank')
    cursor.execute('USE securebank')
    
    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        phone VARCHAR(15),
        password_hash VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status VARCHAR(20) DEFAULT 'active'
    )
    ''')
    
    # Create accounts table (one per user)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        account_number VARCHAR(20) UNIQUE NOT NULL,
        balance DECIMAL(15,2) DEFAULT 0.00,
        currency VARCHAR(5) DEFAULT 'USD',
        account_type VARCHAR(20) DEFAULT 'Savings',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    )
    ''')
    
    # Create transactions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INT AUTO_INCREMENT PRIMARY KEY,
        account_id INT NOT NULL,
        type VARCHAR(20) NOT NULL,
        amount DECIMAL(15,2) NOT NULL,
        description VARCHAR(255),
        recipient_account VARCHAR(20),
        recipient_name VARCHAR(100),
        balance_after DECIMAL(15,2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status VARCHAR(20) DEFAULT 'completed',
        FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
    )
    ''')
    
# Create admins table


    # Sample admin for admins table
    password_plain = b'admin123'
    password_hash = bcrypt.hashpw(password_plain, bcrypt.gensalt()).decode('utf-8')

    cursor.execute("SELECT admin_id FROM admins WHERE email = %s", ('admin@securebank.com',))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO admins (full_name, email, password_hash) VALUES (%s, %s, %s)",
            ('SecureBank Admin', 'admin@securebank.com', password_hash)
        )
        print('Sample admin created: admin@securebank.com / admin123')
    else:
        print('Sample admin already exists.')
    # Add sample admin user if not exists
    password_plain = b'admin123'
    password_hash = bcrypt.hashpw(password_plain, bcrypt.gensalt()).decode('utf-8')
    
    cursor.execute("SELECT user_id FROM users WHERE email = %s", ('admin@example.com',))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users (full_name, email, phone, password_hash) VALUES (%s, %s, %s, %s)",
            ('Admin User', 'admin@example.com', '1234567890', password_hash)
        )
        user_id = cursor.lastrowid
        
        # Create default account
        account_number = '12345678901234567890'
        cursor.execute(
            "INSERT INTO accounts (user_id, account_number, balance) VALUES (%s, %s, %s)",
            (user_id, account_number, 1000.00)
        )
        print('Sample admin user created: admin@example.com / admin123 (Account: ' + account_number + ', Balance: $1000)')
    else:
        print('Sample admin user already exists.')
    
    conn.commit()
    cursor.close()
    conn.close()
    print('Database and tables (users, accounts, transactions) created successfully!')
except Exception as e:
    print(f'Error: {e}')
