# Adam Jahani - Modern Personal CV Website

A professional, interactive, and visually stunning personal CV website showcasing Adam Jahani's education, skills, experience, and projects with modern web technologies and animations.

## 🚀 New Features & Enhancements

### ✨ Visual Enhancements
- **Particle Background Animation**: Interactive floating particles with connections
- **Modern Gradient Design**: Beautiful gradient backgrounds and glassmorphism effects
- **Dark/Light Mode Toggle**: Seamless theme switching with persistent preferences
- **Smooth Animations**: CSS transitions, hover effects, and scroll-triggered animations
- **Enhanced Typography**: Modern Inter font with improved readability
- **Responsive Design**: Mobile-first approach with adaptive layouts

### 🎯 Interactive Features
- **Dynamic Typing Animation**: Rotating text showcasing different roles
- **Animated Skill Bars**: Progressive skill level visualization with shimmer effects
- **Interactive Project Cards**: Hover effects, overlays, and modal previews
- **Timeline Layout**: Modern timeline for education and experience
- **Enhanced Navigation**: Fixed navigation with smooth scrolling
- **Contact Form Validation**: Real-time form validation with error handling

### 🛠️ Technical Improvements
- **Modern CSS Architecture**: CSS Custom Properties, Grid, Flexbox
- **JavaScript Interactivity**: ES6+ features, animations, and user interactions
- **Build System**: Python-based build scripts for optimization
- **Development Server**: Custom development server with live reload
- **Modular Structure**: Organized file structure for maintainability

## 🌟 Features

- **Professional Design**: Clean, modern layout with stunning visual effects
- **Two Pages**: Enhanced main CV page and dedicated contact form
- **Interactive Elements**: Animated components, smooth transitions, theme toggle
- **Project Showcase**: Enhanced project cards with technology tags and action buttons
- **Enhanced Contact Form**: Real-time validation and improved user experience
- **Social Integration**: Social media links and sharing capabilities
- **Performance Optimized**: Minified CSS/JS and optimized assets

## 🚀 Quick Start

### Method 1: Using the Development Script (Recommended)

```bash
# Navigate to the project directory
cd PersonalCV

# Start development server
./scripts/dev.sh serve

# Build for production
./scripts/dev.sh build

# Prepare for deployment
./scripts/dev.sh deploy

# Clean build artifacts
./scripts/dev.sh clean
```

### Method 2: Python HTTP Server

```bash
# Navigate to the project directory
cd PersonalCV

# For Python 3.x (recommended)
python3 -m http.server 8000

# For Python 2.x (if needed)
python -m SimpleHTTPServer 8000
```

Then open your browser and go to: `http://localhost:8000`

### Method 3: Node.js HTTP Server

```bash
# Install a simple HTTP server globally
npm install -g http-server

# Navigate to the project directory and start server
cd PersonalCV
http-server -p 8000
```

### Method 4: Using the Enhanced Development Server

```bash
# Run the enhanced development server directly
python3 scripts/dev-server.py

# Or specify a custom port
python3 scripts/dev-server.py 3000
```

## 📁 Project Structure

```
PersonalCV/
├── index.html              # Enhanced main CV page
├── contact.html            # Enhanced contact form page
├── css/
│   └── style.css          # Modern stylesheet with animations
├── js/
│   └── main.js            # Interactive JavaScript features
├── scripts/
│   ├── dev.sh             # Development workflow script
│   ├── dev-server.py      # Enhanced development server
│   └── build.py           # Build and optimization script
├── images/
│   ├── Headshot.jpg       # Profile photo
│   ├── picture1.jpg       # Data Analysis project image
│   ├── picture2.jpg       # Movie Recommendation project image
│   └── picture3.jpg       # Image Classification project image
├── build/                 # Production build output (generated)
└── README.md              # This file
```

## 🎯 What's Included

### Personal Information
- **Contact Details**: Interactive contact information with copy-to-clipboard
- **Professional Summary**: Dynamic typing animation with role rotation
- **Social Links**: Enhanced social media integration

### Education
- **University Details**: Timeline layout with enhanced visual presentation
- **Academic Achievements**: Organized in modern timeline format

### Honors and Awards
- **Academic Recognition**: Timeline-based presentation
- **Leadership Achievements**: Enhanced descriptions and formatting

### Skills
- **Programming Languages**: Animated progress bars with percentages
- **Frameworks & Libraries**: Categorized skill sets with visual indicators
- **Tools & Technologies**: Interactive skill visualization

### Experience
- **Leadership Roles**: Timeline presentation with detailed descriptions
- **Work Experience**: Enhanced formatting with company links

### Projects
- **Featured Projects**: Interactive cards with hover effects
- **Technology Stack**: Visual tags for technologies used
- **Project Actions**: GitHub links and live demo buttons (ready for real links)

## 🎨 Design Features

### Theme System
- **Dark Mode**: Professional dark theme with proper contrast
- **Light Mode**: Clean light theme for different preferences
- **Smooth Transitions**: Seamless theme switching animations

### Animations & Effects
- **Particle System**: Dynamic background particles with connections
- **Scroll Animations**: Elements animate in as you scroll
- **Hover Effects**: Interactive hover states for all clickable elements
- **Loading States**: Smooth loading animations for form submissions

### Responsive Design
- **Mobile First**: Optimized for mobile devices
- **Tablet Support**: Enhanced layouts for tablet viewing
- **Desktop Experience**: Full-featured desktop presentation

## 🌐 Deployment Options

### GitHub Pages
1. Push your code to a GitHub repository
2. Run `./scripts/dev.sh build` to create production build
3. Go to Settings → Pages in your repository
4. Select source branch (usually `main` or deploy from `/build` folder)
5. Your CV will be available at `https://yourusername.github.io/repository-name`

### Netlify
1. Run `./scripts/dev.sh build` to create production build
2. Drag and drop the `build/` folder onto [Netlify Drop](https://app.netlify.com/drop)
3. Or connect your GitHub repository for automatic deployments

### Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Run `./scripts/dev.sh build`
3. Run `vercel build/` in the project directory
4. Follow the prompts

### Traditional Web Hosting
1. Run `./scripts/dev.sh build`
2. Upload all files from the `build/` directory to your web hosting service
3. Your CV will be available at your domain

## 🛠️ Development

### Building the Project
```bash
# Development build with source maps
./scripts/dev.sh build

# Production build with optimization
./scripts/dev.sh deploy
```

### Customization Guide

#### Personal Information
1. Edit `index.html` to update personal details, education, and experience
2. Replace images in `images/` folder with your own photos
3. Update social media links and contact information

#### Styling
1. Modify CSS custom properties in `css/style.css` for theme colors
2. Adjust animations and transitions to your preference
3. Add or modify sections as needed

#### Functionality
1. Update `js/main.js` to modify interactive features
2. Add your own project links and live demo URLs
3. Integrate with real contact form services (Formspree, Netlify Forms, etc.)

#### Adding New Sections
1. Add HTML structure in `index.html`
2. Style with CSS following the existing pattern
3. Add JavaScript interactions if needed

## 📧 Contact Form Integration

The contact form is currently set up for frontend validation. To make it fully functional:

### Option 1: Formspree Integration
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" class="contact-form">
```

### Option 2: Netlify Forms
```html
<form name="contact" netlify class="contact-form">
```

### Option 3: Custom Backend
Integrate with your preferred backend service or API.

## 🔧 Browser Support

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Mobile**: iOS Safari, Chrome Mobile, Samsung Internet
- **Progressive Enhancement**: Graceful degradation for older browsers

## 📱 Performance

- **Optimized Assets**: Minified CSS and JavaScript
- **Efficient Animations**: Hardware-accelerated CSS animations
- **Responsive Images**: Properly sized images for different devices
- **Lazy Loading**: Scroll-triggered animations and effects

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own use. If you have suggestions for improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🆘 Support

If you encounter any issues:

1. Check the browser console for JavaScript errors
2. Ensure you're running the development server (not opening files directly)
3. Verify all assets are loading properly
4. Check browser compatibility

## 🎉 Acknowledgments

- **Design Inspiration**: Modern web design trends and best practices
- **Icons**: Font Awesome for beautiful icons
- **Fonts**: Google Fonts for typography
- **Animations**: CSS3 and modern JavaScript techniques