# Projects Section Guidelines

## Data Structure

Projects are defined in `js/projects.js` as an array of objects:

```javascript
{
  title: "Project Title",
  description: "Brief description of what the project does",
  tags: ["Tag1", "Tag2", "Tag3"],
  link: "projects/project-slug.html",
  image: "path/to/preview-image.png",
  featured: true
}
```

## Project Page Structure

Each project has a dedicated HTML page in `projects/` folder using the sidebar layout:

```
projects/
  project-slug.html
  project-slug/
    image1.png
    image2.png
```

### HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Project Title - Ahmadreza Nazari</title>
  <link rel="stylesheet" href="../css/styles.css" />
  <!-- KaTeX if math needed -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" />
</head>
<body>
  <div class="layout">
    <!-- Sidebar (same as index.html) -->
    <aside class="sidebar">...</aside>
    
    <!-- Main Content -->
    <main class="main-content">
      <article class="project-detail">
        <a href="../index.html" class="back-link">Back to Home</a>
        
        <header class="project-header">
          <h1>Project Title</h1>
          <div class="project-meta">
            <span class="project-date">Month YYYY</span>
          </div>
          <div class="project-tags">
            <span class="tag">Tag1</span>
          </div>
        </header>

        <div class="project-content">
          <!-- Content sections -->
        </div>
      </article>
    </main>
  </div>
</body>
</html>
```

## Content Sections

Use these classes for content organization:

- `<p>` - Regular paragraphs
- `<h2>` - Section headings
- `<pre><code>` - Code blocks
- `<div class="project-image">` - Image wrapper with caption
- `<ul>`, `<ol>` - Lists

### Images

```html
<div class="project-image">
  <img src="project-slug/image.png" alt="Description" />
  <p class="image-caption">Caption text</p>
</div>
```

### Code Blocks

```html
<pre><code class="language-python">
# Code here
</code></pre>
```

### Math (KaTeX)

Include KaTeX CSS and JS, then use:
- Inline: `\( equation \)`
- Block: `$$ equation $$`

## Layout Rules

- Project preview image appears after description, before detailed content
- Tags appear in project-header after date
- Sidebar remains consistent with index.html

## Styling Notes

- Images have `border-radius: 0.5rem` and subtle shadow
- Code blocks have dark background with proper syntax highlighting colors
- Section headings (`h2`) have `margin-top: 2rem`

## Content Rules

- No emojis
- Technical accuracy is critical
- Include relevant skills/technologies naturally
- Show methodology and results
- Use real repository images when available

## Asset Organization

- Store project-specific images in `projects/project-slug/` folder
- Use descriptive filenames: `gui-screenshot.png`, `training-curve.png`
- Optimize images for web (reasonable file sizes)

## Featured Projects

Set `featured: true` in projects.js for projects to highlight on homepage.
