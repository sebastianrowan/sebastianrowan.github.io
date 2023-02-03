---
layout: page
title: Connect N
description: Random Connect 4
img: assets/img/milos-tomasevic-f0QATZfOTv8-unsplash.jpg
importance: 1
category: fun
---


{% if site.data.repositories.github_repos %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% if repo == "sebastianrowan/connect_n" %}
    {% include repository/repo.html repository=repo %}
    {% endif %}
  {% endfor %}
</div>
{% endif %}

