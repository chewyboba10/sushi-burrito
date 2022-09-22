---
toc: true
layout: post
description: Lecture Notes August 31, 2022
categories: [T1, Notes, Week 2, markdown, post]
title: Lecture Notes - HTML Fragments
author: Evan Aparri
show_tags: true
comments: true
---

# Lecture Notes - HTML Fragments

> What Lists, Dictionaries, and Iterations are and how to use them

## HTML Fragments

procedural abstraction and data abstraction - taking little pieces of information and putting them into different files so that something can take it in the bigger system

markdown gets converted into html.
everything in your website gets converted to html.

## HTML Write Analysis

The theme of the Blog could be changed in the `_config.yml` file in the home directory of the blog. Either `theme` or `remote_theme` key pair value can be altered. The `remote_theme` method needs to have the `jekyll-remote-theme` to be defined in the `plugins` key. I decided to change to the midnight theme because I thought the theme name sounded cool. 

I ran into a minor problem of naming the remote theme wrong, but that was quickly fixed

![]({{ site.baseurl }}/images/theme-mistake.png "Mistake in writing the version name of the theme")

Here is what the homepage looked like:

![]({{ site.baseurl }}/images/midnight-theme.png "Blog with midnight theme")

The problems that I noticed were that the changes removed the blog's navigation bar such as the search and tabs. That is the main problem I saw. When opening some of my posts, they were no negatively affected, but you are unable to open the homepage once you have left:

![]({{ site.baseurl }}/images/no-homepage-access.png "Unable to go back to homepage")

One last thing that I noticed before I changed back to the `minima` theme is that the icon of the blog does not show up. The conclusion that I came from this experiment is that other Jekyll themes are not entirely compatible with fastpages and that `minima` is the preferred theme.