---
layout: page
title: Estimating the Greenhouse Gas Emissions of Flood Damages
description: 
img: assets/img/wes-warren-ZNJFrCOCcKA-unsplash.jpg
importance: 1
category: work
display_categories: [paper, poster, presentation, other]
horizontal: false
---
{%- if true %}
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}

{%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <div class="grid">
    {%- for project in categorized_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>

{%- endfor %}

{%- endif -%}
</div>
{%- endif -%}

<!-- Change to false to true -->
{%- if false %}

<div class="grouped-projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_group_projects = site.grouped_projects | where: "category", category -%}
  <!-- {%- assign sorted_group_projects = categorized_group_projects | sort: "importance" %} -->
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