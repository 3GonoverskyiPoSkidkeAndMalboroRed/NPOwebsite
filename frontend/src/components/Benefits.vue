<script setup lang="ts">
import TaskBlock from "@/components/TaskBlock.vue";
import { RouterLink } from "vue-router";

interface ApplicationProps {
  title: string;
  image: string;
  link: string;
}

const applications: ApplicationProps[] = [
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

<template>
  <section
    id="benefits"
    class="container px-4 sm:px-6 lg:px-8 py-16 sm:py-20 md:py-24 lg:py-32"
  >
    <div class="text-center mb-12 sm:mb-16">
      <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">
        Области применения и решаемые задачи
      </h2>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-3 sm:gap-4">
      <TaskBlock
        v-for="application in applications"
        :key="application.title"
        :task="application"
      />
    </div>

    <div class="text-center mt-8 sm:mt-12">
      <RouterLink
        to="/tasks"
        class="inline-flex items-center justify-center px-6 py-3 text-sm sm:text-base font-medium text-white bg-primary rounded-lg hover:bg-primary/90 transition-colors duration-300"
      >
        Подробнее
      </RouterLink>
    </div>
  </section>
</template>
