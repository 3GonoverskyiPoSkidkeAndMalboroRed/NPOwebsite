<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
            Решаемые задачи
          </h1>

        </div>

        <!-- Основные категории задач -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <TaskBlock
            v-for="task in tasks"
            :key="task.title"
            :task="task"
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import TaskBlock from "@/components/TaskBlock.vue";

interface TaskItem {
  title: string;
  image: string;
  link: string;
}

const tasks: TaskItem[] = [
  {
    title: "Оборудование для экспертизы",
    image: "/home-photo/expertlittle.png",
    link: "/methods-expert"
  },
  {
    title: "Нефтехимия",
    image: "/home-photo/4d3fc1ac61ed98d7a6eb1d8d9e6f7267.png",
    link: "/methods-oil"
  },
  {
    title: "Экология",
    image: "/home-photo/ecologylittle.png",
    link: "/methods-eco"
  },
  {
    title: "Горнорудная промышленность",
    image: "/home-photo/gornlittle.png",
    link: "/methods-mining"
  },
  {
    title: "Металлургия",
    image: "/home-photo/metlittle.png",
    link: "/methods-metallurgy"
  },
  {
    title: "Диагностика и контроль",
    image: "/home-photo/diagnostikalittle2.png",
    link: "/methods-diagnostics"
  },
  {
    title: "Геология",
    image: "/home-photo/geologylittle.png",
    link: "/methods-geology"
  },
  {
    title: "Научные исследования",
    image: "/home-photo/researchlittle.png",
    link: "/methods-research"
  },
  {
    title: "Газовая промышленность",
    image: "/home-photo/06bba93af58b01ffc5367e30d6485f7c.png",
    link: "/methods-gas"
  }
];
</script>