<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section - Auto-reload test -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">
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
    image: "/photostock/Оборудование для эспертизы.jpg",
    link: "/methods-expert"
  },
  {
    title: "Нефтехимия",
    image: "/photostock/Нефтехимия.jpg",
    link: "/methods-oil"
  },
  {
    title: "Экология",
    image: "/photostock/Экология.jpg",
    link: "/methods-eco"
  },
  {
    title: "Горнорудная промышленность",
    image: "/photostock/Горнорудная промышленность.png",
    link: "/methods-mining"
  },
  {
    title: "Металлургия",
    image: "/photostock/Металлургия.png",
    link: "/methods-metallurgy"
  },
  {
    title: "Диагностика и контроль",
    image: "/photostock/Диагностика и контроль.jpg",
    link: "/methods-diagnostics"
  },
  {
    title: "Геология",
    image: "/photostock/Геология.jpg",
    link: "/methods-geology"
  },
  {
    title: "Научные исследования",
    image: "/photostock/Научные исследования.png",
    link: "/methods-research"
  },
  {
    title: "Газовая промышленность",
    image: "/photostock/Газовая промышленность.png",
    link: "/methods-gas"
  }
];
</script>