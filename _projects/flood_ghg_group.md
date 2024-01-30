---
layout: page
title: Estimating the Greenhouse Gas Emissions of Flood Damages
description: 
img: assets/img/wes-warren-ZNJFrCOCcKA-unsplash.jpg
importance: 1
category: work
display_categories: [paper, poster, presentation, other]
group_parent: true
group_id: flood_ghg
horizontal: false
---

<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign grouped_projects = site.projects | where: "group_id", page.group_id -%}
  {%- assign categorized_projects = grouped_projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projects without categories -->
  {%- assign grouped_projects = site.projects | where: "group_id", page.group_id -%}
  {%- assign sorted_projects = grouped_projects | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>

