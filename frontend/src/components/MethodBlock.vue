<template>
  <div class="bg-card rounded-lg border p-8 hover:shadow-lg transition-shadow">
    <div class="flex items-start gap-6">
      <div class="flex-shrink-0">
        <img
          :src="method.image"
          :alt="method.title"
          class="w-24 h-24 object-cover rounded-lg"
        />
      </div>
      <div class="flex-1">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold text-primary">{{ method.title }}</h2>
          <RouterLink
            :to="method.link"
            class="text-primary hover:text-primary/80 font-medium"
          >
            Подробнее →
          </RouterLink>
        </div>
        <p class="text-muted-foreground mb-4">
          {{ method.description }}
        </p>
        <ul class="space-y-2 text-sm">
          <li 
            v-for="item in method.items" 
            :key="item"
            class="flex items-center gap-2"
          >
            <span class="w-2 h-2 bg-primary rounded-full"></span>
            {{ item }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { RouterLink } from "vue-router";

interface MethodItem {
  title: string;
  image: string;
  link: string;
  description: string;
  items: string[];
}

defineProps<{
  method: MethodItem;
}>();
</script>
