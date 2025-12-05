// Main JavaScript
document.addEventListener('DOMContentLoaded', function() {
  // Set current year in footer
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Apply config settings
  if (typeof siteConfig !== 'undefined' && siteConfig.max_width) {
    document.documentElement.style.setProperty('--content-max-width', siteConfig.max_width);
  }

  // Load featured projects on homepage
  loadFeaturedProjects();

  // Load blog posts
  loadBlogPosts();

  // Reveal main content after loading
  const mainContent = document.querySelector('.main-content');
  if (mainContent) mainContent.classList.add('loaded');
});

// Load featured projects from data
function loadFeaturedProjects() {
  const container = document.getElementById('featured-projects-container');
  if (!container) return;

  if (typeof projectsData !== 'undefined' && projectsData.length > 0) {
    const sorted = [...projectsData].sort((a, b) => new Date('1 ' + b.date) - new Date('1 ' + a.date));
    const featured = sorted.filter(p => p.featured);
    container.innerHTML = featured.map(project => `
      <article class="project-card">
        <h3>${project.title}</h3>
        <p class="project-date">${project.date}</p>
        <p>${project.description}</p>
        ${project.preview ? `<div class="project-preview"><img src="${project.preview}" alt="${project.title}" /></div>` : ''}
        <p class="project-tags">${project.tags.map(tag => `<span>${tag}</span>`).join('')}</p>
        <p class="project-links">
          ${project.page ? `<a href="${project.page}">Read more</a>` : ''}
          ${project.github ? `<a href="${project.github}" target="_blank">GitHub</a>` : ''}
          ${project.report ? `<a href="${project.report}" target="_blank">Report</a>` : ''}
          ${project.demo ? `<a href="${project.demo}" target="_blank">Demo</a>` : ''}
        </p>
      </article>
    `).join('');
  }
}

// Load blog posts from data
function loadBlogPosts() {
  const container = document.getElementById('featured-blog-container');
  if (!container) return;

  if (typeof blogData !== 'undefined' && blogData.length > 0) {
    const featured = blogData.slice(0, 2);
    container.innerHTML = featured.map(post => `
      <article class="blog-card">
        <h3>${post.title}</h3>
        <p class="blog-date">${post.date}</p>
        <p>${post.description}</p>
        <p class="blog-keywords">${post.keywords.map(kw => `<span>${kw}</span>`).join('')}</p>
        <p class="blog-links">
          <a href="${post.page}">Read more</a>
        </p>
      </article>
    `).join('');
  }
}
