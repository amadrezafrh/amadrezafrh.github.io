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
  if (typeof projectsData === 'undefined' || projectsData.length === 0) return;

  const sorted = [...projectsData].sort((a, b) => new Date('1 ' + b.date) - new Date('1 ' + a.date));
  const featured = sorted.filter(p => p.featured);

  const linkBtn = (href, label, external) => href
    ? `<a class="project-link" href="${href}"${external ? ' target="_blank" rel="noopener"' : ''}>${label}</a>`
    : '';

  const cardHTML = project => `
    <article class="project-card">
      <div class="project-card-body">
        <h3>${project.title}</h3>
        <p class="project-date">${project.date}</p>
        <p>${project.description}</p>
        ${project.preview ? `<div class="project-preview"><img src="${project.preview}" alt="${project.title}" /></div>` : ''}
        <p class="project-tags">${project.tags.map(tag => `<span>${tag}</span>`).join('')}</p>
      </div>
      <div class="project-links">
        ${linkBtn(project.page, 'Read more', false)}
        ${linkBtn(project.github, 'GitHub', true)}
        ${linkBtn(project.report, 'Report', true)}
        ${linkBtn(project.demo, 'Demo', true)}
      </div>
    </article>
  `;

  const isRail = container.closest('.right-rail') !== null;

  if (!isRail) {
    container.innerHTML = featured.map(cardHTML).join('');
    return;
  }

  // 2-column rail with independent column heights (masonry-style flow).
  // Cards are alternated between the two columns and each card carries a
  // flex `order` equal to its date index. This means:
  //   - at normal zoom the cards inside each column flow in date order
  //     (DOM order matches `order` within a column) so reading left-to-right
  //     across rows is row-wise by date.
  //   - at collapse the masonry-col wrappers become `display: contents` and
  //     the cards become direct flex children of `.projects-grid`
  //     (flex-direction: column). The flex container then re-sorts them by
  //     `order`, stacking the cards in pure date order.
  container.innerHTML = '<div class="masonry-col"></div><div class="masonry-col"></div>';
  const colA = container.children[0];
  const colB = container.children[1];
  featured.forEach((project, i) => {
    const tmp = document.createElement('div');
    tmp.innerHTML = cardHTML(project).trim();
    const card = tmp.firstChild;
    card.style.order = i;
    (i % 2 === 0 ? colA : colB).appendChild(card);
  });
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
