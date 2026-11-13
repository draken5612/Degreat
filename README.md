# DE-GREAT WELD ENTERPRISES - Professional Website

A fully functional, modern, and SEO-optimized website for DE-GREAT WELD ENTERPRISES - Nigeria's leading metalworking and equipment rental company.

## 🌟 Features

### Core Services
- **Welding Services**: Argon welding, stainless steel welding, mild steel welding, and custom fabrication
- **Generator Rentals**: Industrial, petrol, diesel, and gas-powered generators with real-time pricing
- **Scaffold Rentals**: Construction, access, and modular scaffolding solutions
- **Welder Hiring**: Professional job application portal for welders

### Website Features
- ✅ Responsive design (mobile-first approach)
- ✅ Professional blue & white theme
- ✅ Fast page load times (optimized for performance)
- ✅ SEO-optimized (meta tags, schema markup, structured data)
- ✅ WhatsApp integration with pre-filled messages
- ✅ Contact forms with email notifications
- ✅ Portfolio/project gallery
- ✅ Admin dashboard for managing content
- ✅ Google Analytics ready
- ✅ HTTPS ready (SSL/TLS support)

### Services Available
- Welding service details with specifications
- Generator rental inquiries and booking
- Scaffold rental requests
- Welder job applications with CV upload
- Contact form for general inquiries
- FAQ page
- Privacy policy and terms & conditions

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- git (optional)

## 🚀 Installation & Setup

### 1. Extract the Project
```bash
unzip degreat_weld_project.zip
cd degreat_weld_project
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example env file
cp .env.example .env

# Edit .env file with your settings
# Update:
# - SECRET_KEY (generate a new one)
# - COMPANY_PHONE (your phone number)
# - COMPANY_WHATSAPP (your WhatsApp number)
# - COMPANY_EMAIL (your email)
# - Other settings as needed
```

### 5. Initialize Database
```bash
# Create database tables
python manage.py migrate

# Populate with sample data (services, generators, scaffolds, projects)
python manage.py populate_data

# Create admin user
python manage.py createsuperuser
# Follow prompts to create your admin account
```

### 6. Collect Static Files (for production)
```bash
python manage.py collectstatic --noinput
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

Admin dashboard: `http://localhost:8000/admin`

---

## 📝 Customization Guide

### Update Company Information

Edit `degreat_config/settings.py`:
```python
COMPANY_NAME = "DE-GREAT WELD ENTERPRISES"
COMPANY_EMAIL = "your-email@degreatwelds.com"
COMPANY_PHONE = "+234-XXX-XXX-XXXX"
COMPANY_WHATSAPP = "+234XXXXXXXXXX"
COMPANY_ADDRESS = "Ikorodu, Lagos State, Nigeria"
```

### Add Your Logo & Branding

1. Upload your logo to: `static/images/logo.png`
2. Update `templates/base.html` navbar branding section
3. Update colors in `static/css/style.css` (CSS variables at top)

### Update Services

1. Go to admin: `/admin`
2. Login with your superuser account
3. Navigate to "Services & Rentals"
4. Click "Services" to add/edit welding services
5. Add images, descriptions, and specifications

### Manage Generators & Scaffolds

1. Admin > "Services & Rentals"
2. Manage "Generators" and "Scaffolds"
3. Set pricing (daily/weekly/monthly rates)
4. Add images and specifications

### Upload Project Photos

1. Admin > "Portfolio"
2. Click "Projects" to add new projects
3. Upload project image and gallery images
4. Set featured flag for homepage display

### Manage Welder Applications

1. Admin > "Welder Applications"
2. View submitted applications
3. Download CVs and work samples
4. Update application status

---

## 🌐 Free Deployment to Render

The project includes a `render.yaml` blueprint. To deploy:

1. Create a GitHub repository and upload the contents of this project directory
   (the directory containing `manage.py`). Do not upload `.env`, `db.sqlite3`,
   `venv/`, or the local Django password file; these are excluded by `.gitignore`.
2. Sign in to [Render](https://render.com), choose **New → Blueprint**, and
   connect the repository.
3. Review the `degreat-weld` free web service and deploy it. Render generates
   the production `SECRET_KEY` automatically.
4. Open the service’s `onrender.com` URL after the deploy succeeds.

The free web service uses an ephemeral filesystem and may spin down when idle.
SQLite changes, admin uploads, and form-uploaded files are not durable and can
be lost after a restart or redeploy. Use a persistent database and file-storage
service before relying on the site for live customer submissions.

### 3. Custom Domain Setup

1. In Render dashboard, go to Settings
2. Add your custom domain (e.g., degreatwelds.com.ng)
3. Update domain DNS records per Render instructions

---

## 🔐 Security Checklist

Before going live:

- [ ] Keep `SECRET_KEY` in the hosting provider's environment settings, not in source control
- [ ] Set `DEBUG = False` in the hosting provider's environment settings
- [ ] Set `ALLOWED_HOSTS` to the deployed hostname(s)
- [ ] Enable `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, and `CSRF_COOKIE_SECURE` in production
- [ ] Add HTTPS certificate (Render provides this automatically)
- [ ] Create strong superuser password
- [ ] Regularly backup database
- [ ] Keep dependencies updated

---

## 📧 Email Configuration

To send contact form emails:

1. Edit `.env`:
```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

2. Generate Gmail app password:
   - Go to https://myaccount.google.com/apppasswords
   - Select Mail and Device
   - Copy the generated password

---

## 🔍 SEO Optimization

### Keywords Covered
- Welding services Nigeria
- Metal fabrication Nigeria
- Generator rental Lagos/Ikorodu
- Argon welding services
- Industrial welding contractor
- Scaffold rental Nigeria
- Welder for hire Nigeria

### SEO Features Implemented
- ✅ Optimized meta tags and descriptions
- ✅ Schema markup for local business
- ✅ Mobile-first responsive design
- ✅ Fast page load times
- ✅ XML sitemap ready
- ✅ robots.txt configured
- ✅ Structured data for services
- ✅ Local SEO optimization
- ✅ Google Analytics integration ready

### Next Steps for SEO
1. Submit to Google Search Console
2. Add Google Analytics ID to settings
3. Create Google My Business listing
4. Build backlinks from industry directories
5. Create blog content for keywords

---

## 📞 WhatsApp Integration

Messages are automatically pre-filled based on service selected:

- General inquiry
- Welding service inquiry (Argon, Stainless, Mild)
- Generator rental inquiry
- Scaffold rental inquiry
- Welder hiring inquiry

Update WhatsApp number in:
1. `degreat_config/settings.py` - `COMPANY_WHATSAPP`
2. `templates/base.html` - Footer WhatsApp button
3. All service detail pages

---

## 🛠️ Troubleshooting

### Issue: Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Issue: Database migration error
```bash
python manage.py migrate --fake-initial
```

### Issue: Port already in use
```bash
python manage.py runserver 8001
```

### Issue: Import errors
```bash
pip install -r requirements.txt --upgrade
```

---

## 📱 Mobile Optimization

The website is fully mobile-responsive and optimized for:
- Smartphones (320px+)
- Tablets
- Desktops
- All modern browsers

Test responsiveness at: [Responsive Design Checker](https://responsivedesignchecker.com/)

---

## 💡 Tips & Best Practices

1. **Regular Backups**: Backup database weekly
2. **Update Content**: Keep portfolio and services current
3. **Monitor Analytics**: Check visitor behavior regularly
4. **Respond Quickly**: Reply to inquiries within 24 hours
5. **Add Images**: High-quality project photos boost conversions
6. **Social Media**: Link to Instagram, Facebook pages
7. **Local Listings**: Register on Nigerian business directories
8. **Blog Posts**: Create SEO content about welding, generators
9. **Customer Reviews**: Display testimonials prominently
10. **Test Everything**: Test forms, links, and WhatsApp integration

---

## 📞 Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com
2. Review error messages carefully
3. Check Render logs for deployment issues
4. Verify all settings in `settings.py`

---

## 📄 File Structure

```
degreat_weld_project/
├── degreat_config/          # Django settings
├── core/                    # Home, about, contact pages
├── services/                # Welding, generator, scaffold services
├── portfolio/               # Project gallery
├── applications/            # Welder job applications
├── static/                  # CSS, JavaScript, images
│   ├── css/
│   ├── js/
│   └── images/
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── core/               # Core app templates
│   ├── services/           # Services templates
│   ├── portfolio/          # Portfolio templates
│   └── applications/       # Application templates
├── media/                   # User-uploaded files
├── requirements.txt         # Python dependencies
├── manage.py               # Django management
└── README.md               # This file
```

---

## 🎨 Color Scheme

**Primary Blue**: #0052CC  
**Dark Blue**: #003d99  
**Light Blue**: #E8F0FF  
**White**: #FFFFFF  
**Dark Gray**: #2C3E50  

All CSS variables defined in `static/css/style.css`

---

## ✅ Pre-Launch Checklist

- [ ] All company information updated
- [ ] Logo and branding in place
- [ ] Services with descriptions and images added
- [ ] Generator prices and specs updated
- [ ] Scaffold rental details added
- [ ] Portfolio projects with photos uploaded
- [ ] WhatsApp number verified and working
- [ ] Contact form tested
- [ ] Admin account created
- [ ] Email configuration tested
- [ ] SSL certificate enabled
- [ ] Domain DNS configured
- [ ] Security settings enabled
- [ ] Google Analytics ID added
- [ ] Google My Business listing created

---

## 📞 Contact

**DE-GREAT WELD ENTERPRISES**  
Ikorodu, Lagos State, Nigeria  
📧 Email: info@degreatwelds.com  
📞 Phone: +234-XXX-XXX-XXXX  
💬 WhatsApp: +234XXXXXXXXXX

---

**Created with Django & ❤️ for Professional Excellence**

Last Updated: 2024
