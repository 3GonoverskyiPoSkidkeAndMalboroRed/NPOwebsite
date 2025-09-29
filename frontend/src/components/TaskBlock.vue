<template>
  <RouterLink 
    :to="task.link" 
    class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer"
    :style="{ backgroundImage: `url('${task.image}')` }"
  >
    <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
    <div class="relative z-10">
      <h3 class="text-xl font-semibold text-white">{{ task.title }}</h3>
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
