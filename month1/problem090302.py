# Problem 09.03.02: Template và report generation

print("=== TEMPLATE VÀ REPORT GENERATION ===")

from string import Template
from datetime import datetime

# Bài 1: Email templates
print("1. Email templates:")

email_template = """
Subject: Welcome to {company_name}!

Dear {customer_name},

Thank you for joining {company_name}! We're excited to have you as our customer.

Your account details:
- Username: {username}
- Email: {email}
- Registration Date: {reg_date}
- Account Type: {account_type}

Next steps:
1. Verify your email address
2. Complete your profile
3. Explore our {product_count} products

If you have any questions, please contact our support team at {support_email}.

Best regards,
The {company_name} Team

---
This email was sent to {email}. If you didn't create this account, please ignore this email.
"""

# Customer data
customers = [
    {
        "customer_name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com",
        "account_type": "Premium",
        "reg_date": "2024-01-15"
    },
    {
        "customer_name": "Jane Smith", 
        "username": "janesmith",
        "email": "jane@example.com",
        "account_type": "Basic",
        "reg_date": "2024-01-16"
    }
]

# Company info
company_info = {
    "company_name": "TechCorp",
    "product_count": 150,
    "support_email": "support@techcorp.com"
}

print("Generated emails:")
for i, customer in enumerate(customers, 1):
    # Merge customer and company data
    email_data = {**customer, **company_info}
    
    # Generate email
    email_content = email_template.format(**email_data)
    
    print(f"\n--- Email {i} ---")
    print(email_content[:200] + "..." if len(email_content) > 200 else email_content)

# Bài 2: Invoice template
print("\n2. Invoice template:")

invoice_template = """
{company_name}
{company_address}
Phone: {company_phone} | Email: {company_email}

INVOICE #{invoice_number}
Date: {invoice_date}
Due Date: {due_date}

Bill To:
{customer_name}
{customer_address}

{item_header}
{item_separator}
{item_rows}
{item_separator}
{subtotal_row}
{tax_row}
{total_row}

Payment Terms: {payment_terms}
Thank you for your business!
"""

def generate_invoice(invoice_data):
    """Generate formatted invoice"""
    
    # Format items
    item_header = f"{'Description':<30} {'Qty':>5} {'Price':>10} {'Total':>10}"
    item_separator = "-" * 57
    
    item_rows = []
    subtotal = 0
    
    for item in invoice_data['items']:
        desc = item['description']
        qty = item['quantity']
        price = item['price']
        total = qty * price
        subtotal += total
        
        row = f"{desc:<30} {qty:>5} ${price:>8.2f} ${total:>8.2f}"
        item_rows.append(row)
    
    # Calculate tax and total
    tax_rate = invoice_data.get('tax_rate', 0.08)
    tax_amount = subtotal * tax_rate
    final_total = subtotal + tax_amount
    
    # Format summary rows
    subtotal_row = f"{'Subtotal:':<47} ${subtotal:>8.2f}"
    tax_row = f"{f'Tax ({tax_rate:.1%}):':<47} ${tax_amount:>8.2f}"
    total_row = f"{'TOTAL:':<47} ${final_total:>8.2f}"
    
    # Prepare template data
    template_data = {
        **invoice_data,
        'item_header': item_header,
        'item_separator': item_separator,
        'item_rows': '\n'.join(item_rows),
        'subtotal_row': subtotal_row,
        'tax_row': tax_row,
        'total_row': total_row
    }
    
    return invoice_template.format(**template_data)

# Sample invoice data
invoice_data = {
    'company_name': 'ABC Services Inc.',
    'company_address': '123 Business St, City, State 12345',
    'company_phone': '(555) 123-4567',
    'company_email': 'billing@abcservices.com',
    'invoice_number': 'INV-2024-001',
    'invoice_date': '2024-01-15',
    'due_date': '2024-02-14',
    'customer_name': 'XYZ Corporation',
    'customer_address': '456 Client Ave, City, State 67890',
    'payment_terms': 'Net 30 days',
    'tax_rate': 0.085,
    'items': [
        {'description': 'Web Development', 'quantity': 40, 'price': 75.00},
        {'description': 'Graphic Design', 'quantity': 10, 'price': 50.00},
        {'description': 'Consulting', 'quantity': 5, 'price': 100.00}
    ]
}

print("Generated Invoice:")
print(generate_invoice(invoice_data))

# Bài 3: Report templates với Template class
print("\n3. Report templates với Template class:")

# Monthly report template
monthly_report_template = Template("""
MONTHLY PERFORMANCE REPORT
Company: $company_name
Period: $report_month $report_year

EXECUTIVE SUMMARY
================
Total Revenue: $$$total_revenue
Total Expenses: $$$total_expenses
Net Profit: $$$net_profit
Profit Margin: $profit_margin%

KEY METRICS
===========
New Customers: $new_customers
Customer Retention: $retention_rate%
Average Order Value: $$$avg_order_value
Monthly Growth: $growth_rate%

TOP PERFORMING PRODUCTS
======================
$top_products

RECOMMENDATIONS
===============
$recommendations

Report generated on: $generation_date
""")

def format_top_products(products):
    """Format top products list"""
    lines = []
    for i, (product, revenue) in enumerate(products, 1):
        lines.append(f"{i}. {product}: ${revenue:,.2f}")
    return '\n'.join(lines)

# Sample report data
report_data = {
    'company_name': 'TechStart Inc.',
    'report_month': 'January',
    'report_year': '2024',
    'total_revenue': 125000.00,
    'total_expenses': 95000.00,
    'net_profit': 30000.00,
    'profit_margin': 24.0,
    'new_customers': 45,
    'retention_rate': 92.5,
    'avg_order_value': 275.50,
    'growth_rate': 15.2,
    'top_products': format_top_products([
        ('Premium Software License', 45000.00),
        ('Consulting Services', 32000.00),
        ('Training Package', 18500.00)
    ]),
    'recommendations': '- Focus on customer retention programs\n- Expand premium product line\n- Increase marketing in Q2',
    'generation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}

print("Monthly Report:")
print(monthly_report_template.substitute(report_data))

# Bài 4: Dynamic table generation
print("\n4. Dynamic table generation:")

def create_table(headers, rows, title=None, width_ratios=None):
    """Create formatted table"""
    if not headers or not rows:
        return "Empty table"
    
    # Calculate column widths
    if width_ratios:
        total_width = 80
        col_widths = [int(total_width * ratio) for ratio in width_ratios]
    else:
        col_widths = []
        for i, header in enumerate(headers):
            max_width = len(str(header))
            for row in rows:
                if i < len(row):
                    max_width = max(max_width, len(str(row[i])))
            col_widths.append(max_width + 2)
    
    # Build table
    table_lines = []
    
    # Title
    if title:
        total_width = sum(col_widths) + len(headers) - 1
        table_lines.append(title.center(total_width))
        table_lines.append("=" * total_width)
    
    # Header
    header_line = ""
    for i, (header, width) in enumerate(zip(headers, col_widths)):
        if i > 0:
            header_line += "|"
        header_line += f"{str(header):<{width}}"
    table_lines.append(header_line)
    
    # Separator
    separator = ""
    for i, width in enumerate(col_widths):
        if i > 0:
            separator += "+"
        separator += "-" * width
    table_lines.append(separator)
    
    # Data rows
    for row in rows:
        row_line = ""
        for i, (cell, width) in enumerate(zip(row, col_widths)):
            if i > 0:
                row_line += "|"
            # Right align numbers, left align text
            cell_str = str(cell)
            if isinstance(cell, (int, float)) or (isinstance(cell, str) and cell.replace('.', '').replace(',', '').isdigit()):
                row_line += f"{cell_str:>{width}}"
            else:
                row_line += f"{cell_str:<{width}}"
        table_lines.append(row_line)
    
    return "\n".join(table_lines)

# Sample data for table
sales_data = [
    ["Alice Johnson", "North", 125000, "105%"],
    ["Bob Smith", "South", 98000, "82%"],
    ["Carol Davis", "East", 142000, "118%"],
    ["David Wilson", "West", 87000, "73%"]
]

headers = ["Sales Rep", "Region", "Sales ($)", "Target (%)"]
sales_table = create_table(headers, sales_data, "Q1 2024 SALES PERFORMANCE")
print(sales_table)

# Bài 5: Configuration file generation
print("\n5. Configuration file generation:")

config_template = Template("""
# $app_name Configuration File
# Generated on: $generation_date

[database]
host = $db_host
port = $db_port
name = $db_name
user = $db_user
password = $db_password
pool_size = $db_pool_size

[server]
host = $server_host
port = $server_port
debug = $debug_mode
workers = $worker_count

[logging]
level = $log_level
file = $log_file
max_size = $log_max_size
backup_count = $log_backup_count

[features]
enable_api = $enable_api
enable_web = $enable_web
enable_cache = $enable_cache
cache_ttl = $cache_ttl

[security]
secret_key = $secret_key
session_timeout = $session_timeout
max_login_attempts = $max_login_attempts
""")

# Configuration data for different environments
environments = {
    'development': {
        'app_name': 'MyApp Development',
        'db_host': 'localhost',
        'db_port': 5432,
        'db_name': 'myapp_dev',
        'db_user': 'dev_user',
        'db_password': 'dev_password',
        'db_pool_size': 5,
        'server_host': '127.0.0.1',
        'server_port': 8000,
        'debug_mode': 'true',
        'worker_count': 1,
        'log_level': 'DEBUG',
        'log_file': 'logs/app_dev.log',
        'log_max_size': '10MB',
        'log_backup_count': 3,
        'enable_api': 'true',
        'enable_web': 'true',
        'enable_cache': 'false',
        'cache_ttl': 300,
        'secret_key': 'dev-secret-key-123',
        'session_timeout': 3600,
        'max_login_attempts': 10,
        'generation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    'production': {
        'app_name': 'MyApp Production',
        'db_host': 'prod-db.company.com',
        'db_port': 5432,
        'db_name': 'myapp_prod',
        'db_user': 'prod_user',
        'db_password': '${DB_PASSWORD}',
        'db_pool_size': 20,
        'server_host': '0.0.0.0',
        'server_port': 80,
        'debug_mode': 'false',
        'worker_count': 4,
        'log_level': 'INFO',
        'log_file': '/var/log/myapp/app.log',
        'log_max_size': '100MB',
        'log_backup_count': 10,
        'enable_api': 'true',
        'enable_web': 'true',
        'enable_cache': 'true',
        'cache_ttl': 3600,
        'secret_key': '${SECRET_KEY}',
        'session_timeout': 1800,
        'max_login_attempts': 3,
        'generation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
}

print("Configuration files:")
for env_name, config_data in environments.items():
    print(f"\n--- {env_name.upper()} CONFIG ---")
    config_content = config_template.substitute(config_data)
    # Show first few lines
    lines = config_content.split('\n')
    for line in lines[:15]:
        print(line)
    print("... (truncated)")

# Bài 6: HTML report generation
print("\n6. HTML report generation:")

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background-color: #f0f0f0; padding: 10px; text-align: center; }}
        .summary {{ margin: 20px 0; }}
        .metric {{ display: inline-block; margin: 10px; padding: 10px; border: 1px solid #ccc; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p>Generated on: {generation_date}</p>
    </div>
    
    <div class="summary">
        <h2>Summary</h2>
        {summary_metrics}
    </div>
    
    <div class="data">
        <h2>Detailed Data</h2>
        {data_table}
    </div>
</body>
</html>
"""

def generate_html_report(title, metrics, table_data):
    """Generate HTML report"""
    
    # Generate summary metrics HTML
    metrics_html = ""
    for metric_name, metric_value in metrics.items():
        metrics_html += f'<div class="metric"><strong>{metric_name}:</strong> {metric_value}</div>\n'
    
    # Generate table HTML
    if table_data and 'headers' in table_data and 'rows' in table_data:
        table_html = "<table>\n<tr>\n"
        for header in table_data['headers']:
            table_html += f"<th>{header}</th>\n"
        table_html += "</tr>\n"
        
        for row in table_data['rows']:
            table_html += "<tr>\n"
            for cell in row:
                table_html += f"<td>{cell}</td>\n"
            table_html += "</tr>\n"
        table_html += "</table>"
    else:
        table_html = "<p>No data available</p>"
    
    # Generate final HTML
    html_content = html_template.format(
        title=title,
        generation_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        summary_metrics=metrics_html,
        data_table=table_html
    )
    
    return html_content

# Sample HTML report
html_metrics = {
    "Total Sales": "$125,000",
    "Orders": "450",
    "Average Order": "$278",
    "Growth": "+15.2%"
}

html_table_data = {
    "headers": ["Product", "Sales", "Units", "Growth"],
    "rows": [
        ["Laptop Pro", "$45,000", "45", "+20%"],
        ["Wireless Mouse", "$8,500", "340", "+5%"],
        ["Keyboard", "$12,000", "160", "+12%"]
    ]
}

html_report = generate_html_report("Monthly Sales Report", html_metrics, html_table_data)
print("HTML Report generated (first 500 characters):")
print(html_report[:500] + "...")