---
toc: true
comments: true
layout: post
title: Final Thougts
author: Spencer Lyons
nav: nav/home.html
comments: false
---

# What I Learned from Building Bitshift 0101

Bitshift 0101 was an experimental project designed to teach binary concepts through a visual and interactive environment. In this blog post, I want to reflect on what I learned throughout development—from low-level computing fundamentals to visual design and educational systems. This project became a deep dive into how binary operations really work and how to make them understandable, hands-on, and even fun.

---

## Demo Video

Here's a short video walkthrough of Bitshift 0101 in action:

<div style="margin-top: 40px; width: 100%; max-width: 900px; display: flex; justify-content: center;">
  <div style="position: relative; padding-bottom: 56.25%; height: 0; width: 100%; max-width: 800px;">
    <iframe 
      src="https://www.youtube.com/embed/x7uzsDoNcd4" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen 
      style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 12px; box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);">
    </iframe>
  </div>
</div>

---

## Understanding Binary Fundamentals

One of the first things I had to revisit was the binary number system itself. Although I had a surface-level understanding of binary before this project, building Bitshift 0101 required me to dig deep into how binary actually represents data, and how bitwise operations function at a mechanical level.

To help users learn:

- I created a system where each bit is represented as a square that visibly toggles on (1) or off (0).
- I manually implemented binary-to-decimal and decimal-to-binary conversions to better understand the math behind the scenes.
- Logical operations like **AND**, **OR**, **XOR**, and **NOT** were implemented visually, and I had to ensure they behaved correctly no matter the bit width.

This taught me how computers represent everything—from numbers to characters—using only high and low voltage states. It also gave me a new appreciation for the simplicity and elegance of binary math.

<!-- add image -->

---

## Interactive Logic and Simulation

After setting up basic binary representation, the next challenge was giving users the ability to manipulate data interactively. I wanted to replicate the feeling of "wiring up" a digital circuit without any hardware.

This section included:

- Creating **custom logic gates** that respond in real-time to bit inputs, allowing users to build their own circuits using drag-and-drop tools or toggles.
- Implementing **bit shifting** operations (`<<` and `>>`) as animations that slide bit values across cells, mimicking what happens at the hardware level.
- Building a **dependency graph** between logic elements, where each change would cascade and update connected elements in the correct order.

The process helped me understand how logic simulators work behind the scenes—how inputs must be managed, events queued, and outputs recalculated precisely. It was like creating a digital sandbox version of an actual circuit simulator.

<!-- add image -->

---

## Visualizing Binary Data

Making binary data look beautiful was one of the most surprising challenges. At its core, binary is abstract—just 0s and 1s—but I wanted to turn it into a tactile and visually engaging experience.

Some key design choices included:

- Using **color-coded tiles** to represent active and inactive bits in a way that’s easy to scan at a glance.
- Including **motion and animation** to make operations feel alive—shifts slide, gates flash, and outputs glow briefly.
- Keeping a **clean grid-based layout** to reduce visual clutter and emphasize structure.

I found that visual clarity and smooth feedback loops are just as important as functionality. This was a lesson in **user-centered design**—how to take something dry like bitwise math and make it both intuitive and satisfying to play with.

<!-- add image -->

---

## Tools and Technologies Used

Bitshift 0101 was built entirely using web technologies, which allowed it to run in the browser and remain easily accessible. Here’s what I used and why:

- **JavaScript and the Canvas API** were used for rendering the bits, logic gates, and animations. The Canvas API gave me pixel-level control and good performance.
- **HTML/CSS** provided the UI framework, which I kept intentionally minimal to focus attention on the binary logic.
- I built a **custom event system** so that each component (bit, gate, switch) could communicate with others efficiently. This helped simulate how real electronics pass signals through wires.
- I also tested parts of the system in **Turbowarp**, a Scratch variant, to explore educational reach and see how the concepts could translate to a block-based programming audience.

By building the entire system from scratch without relying on existing logic libraries or engines, I gained a stronger understanding of low-level rendering and dataflow management.

<!-- add image -->

---

## Teaching What I Learned

One of the most rewarding aspects of this project was realizing that I wasn’t just learning—I was building something that could teach others too.

To support this goal:

- I wrote clear documentation for how each component worked, including internal logic and visual behavior.
- I added **step-by-step tutorials** and interactive hints that walk users through performing basic binary tasks.
- I created a set of **challenges** that gradually increase in complexity—from toggling single bits to combining multiple gates into small programs.

Designing educational tools made me think deeply about **how people learn**, and what makes a concept truly “click.” I learned to think from the user’s perspective and guide them through confusion toward understanding.

<!-- add image -->

---

## Final Thoughts

Bitshift 0101 started as a small experiment, but it quickly evolved into something much larger—a combination of engineering, design, and pedagogy. Through building it, I gained a renewed appreciation for the binary system and how it's the foundation of everything in computing.

It also showed me how powerful interactive learning tools can be, and how much value there is in making the invisible inner workings of computers visible and tangible.

If you're curious about how computers think at their core—or if you're looking for a hands-on way to learn binary—this project was made for you.
