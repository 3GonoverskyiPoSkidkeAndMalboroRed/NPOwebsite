<script setup lang="ts">
import { Card, CardHeader, CardTitle } from "@/components/ui/card";
import { RouterLink } from "vue-router";

interface ApplicationProps {
  title: string;
  image: string;
  link: string;
}

const applications: ApplicationProps[] = [
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

<template>
  <section
    id="benefits"
    class="container py-24 sm:py-32"
  >
    <div class="text-center mb-16">
      <h2 class="text-3xl md:text-4xl font-bold mb-4">
        Области применения и решаемые задачи
      </h2>
    </div>

    <div class="grid sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-3 gap-3">
      <RouterLink
        v-for="application in applications"
        :key="application.title"
        :to="application.link"
        class="block"
      >
        <Card class="group hover:shadow-lg transition-all duration-300 overflow-hidden cursor-pointer">
          <div class="relative h-32 overflow-hidden">
            <img
              :src="application.image"
              :alt="application.title"
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
            />
            <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors duration-300"></div>
          </div>
          
          <CardHeader class="pb-2 px-3">
            <CardTitle class="text-sm text-center group-hover:text-primary transition-colors duration-300 leading-tight">
              {{ application.title }}
            </CardTitle>
          </CardHeader>
        </Card>
      </RouterLink>
    </div>

    <div class="text-center mt-12">
      <RouterLink
        to="/tasks"
        class="inline-flex items-center justify-center px-6 py-3 text-base font-medium text-white bg-primary rounded-lg hover:bg-primary/90 transition-colors duration-300"
      >
        Подробнее
      </RouterLink>
    </div>
  </section>
</template>
