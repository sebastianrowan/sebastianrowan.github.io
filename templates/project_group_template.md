---
layout: page
title: Project Group 1
description: A set of projects with a common theme
img: assets/img/12.jpg
importance: 1
category: work
display_categories: [papers, presentations, other]
horizontal: false
---

{%- if false %}

<div class="grouped-projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_group_projects = site.grouped_projects | where: "category", category -%}
  {%- assign sorted_group_projects = categorized_group_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_group_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_group_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}

<!-- Display projects without categories -->

  {%- assign sorted_group_projects = site.grouped_projects | sort: "importance" -%}

<!-- Generate cards for each project -->

  {% if page.horizontal -%}

<div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_group_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_group_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>

{%- endif -%}
