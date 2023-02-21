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

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/connect_n/game.png" title="game screenshot" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Screenshot of the gameboard
</div>