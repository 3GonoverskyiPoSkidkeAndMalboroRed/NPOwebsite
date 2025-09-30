<template>
  <RouterLink 
    :to="task.link" 
    class="block relative rounded-lg p-6 border hover:shadow-lg transition-all duration-300 overflow-hidden cursor-pointer h-48 flex items-center justify-center"
    :style="{ 
      backgroundImage: `url('${task.image}')`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      backgroundRepeat: 'no-repeat'
    }"
  >
    <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
    <div class="relative z-10 text-center">
      <h3 class="text-xl font-semibold text-white leading-tight">{{ task.title }}</h3>
    </div>
  </RouterLink>
</template>

<script setup lang="ts">
import { RouterLink } from "vue-router";

interface TaskItem {
  title: string;
  image: string;
  link: string;
}

defineProps<{
  task: TaskItem;
}>();
</script>
