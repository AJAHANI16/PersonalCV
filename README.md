# Adam Jahani - Personal CV Website

A professional, responsive personal CV website showcasing Adam Jahani's education, skills, experience, and projects.

## 🌟 Features

- **Professional Design**: Clean, modern layout with responsive design
- **Two Pages**: Main CV page and dedicated contact form
- **Interactive Elements**: Links to LinkedIn, project details, and contact form
- **Project Showcase**: Visual cards displaying key projects with descriptions
- **Contact Form**: Direct email integration for inquiries

## 🚀 How to Run This CV

Since this is a static HTML website, you need to serve it through a web server to view it properly. Here are several ways to run it:

### Method 1: Python HTTP Server (Recommended)

If you have Python installed (most systems do):

```bash
# Navigate to the project directory
cd PersonalCV

# For Python 3.x (recommended)
python3 -m http.server 8000

# For Python 2.x (if needed)
python -m SimpleHTTPServer 8000
```

Then open your browser and go to: `http://localhost:8000`

### Method 2: Node.js HTTP Server

If you have Node.js installed:

```bash
# Install a simple HTTP server globally
npm install -g http-server

# Navigate to the project directory and start server
cd PersonalCV
http-server -p 8000
```

Then open your browser and go to: `http://localhost:8000`

### Method 3: PHP Built-in Server

If you have PHP installed:

```bash
# Navigate to the project directory
cd PersonalCV

# Start PHP built-in server
php -S localhost:8000
```

Then open your browser and go to: `http://localhost:8000`

### Method 4: Live Server Extension (VS Code)

If you're using Visual Studio Code:

1. Install the "Live Server" extension
2. Right-click on `index.html`
3. Select "Open with Live Server"

### Method 5: Using Any Web Server

You can also use any web server software like Apache, Nginx, or others. Simply place the files in your web server's document root and access them through your server.

## 📁 Project Structure

```
PersonalCV/
├── index.html          # Main CV page
├── contact.html        # Contact form page
├── css/
│   └── style.css      # Stylesheet
├── images/
│   ├── Headshot.jpg   # Profile photo
│   ├── picture1.jpg   # Data Analysis project image
│   ├── picture2.jpg   # Movie Recommendation project image
│   └── picture3.jpg   # Image Classification project image
└── README.md          # This file
```

## 🎯 What's Included

- **Personal Information**: Contact details, location, and professional summary
- **Education**: University of Georgia Computer Science program details
- **Honors and Awards**: Academic achievements and recognitions
- **Skills**: Programming languages, frameworks, databases, and tools
- **Experience**: Leadership roles and work experience
- **Projects**: Three featured projects with descriptions:
  - Data Analysis with Python
  - Movie Recommendation System
  - Image Classification with Machine Learning

## 🌐 Deployment Options

### GitHub Pages
1. Push your code to a GitHub repository
2. Go to Settings → Pages
3. Select source branch (usually `main` or `gh-pages`)
4. Your CV will be available at `https://yourusername.github.io/repository-name`

### Netlify
1. Drag and drop the project folder onto [Netlify Drop](https://app.netlify.com/drop)
2. Or connect your GitHub repository for automatic deployments

### Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project directory
3. Follow the prompts

## 🛠️ Customization

To customize this CV for your own use:

1. Edit `index.html` to update personal information, education, skills, and experience
2. Replace images in the `images/` folder with your own photos
3. Modify `css/style.css` to change colors, fonts, or layout
4. Update `contact.html` with your email address in the form action

## 📧 Contact

The contact form is configured to open the default email client. For a more advanced contact form with server-side processing, consider integrating with services like Formspree, Netlify Forms, or similar.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).