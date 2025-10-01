<template>
  <div class="bg-card rounded-lg border p-4 sm:p-6 lg:p-8 hover:shadow-lg transition-shadow">
    <div class="flex flex-col sm:flex-row items-start gap-4 sm:gap-6">

      <div class="flex-1 w-full">
        <div class="flex items-center justify-between mb-3 sm:mb-4">
          <h2 class="text-lg sm:text-xl lg:text-2xl font-bold text-primary">{{ method.title }}</h2>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-3 sm:gap-4">
          <RouterLink
            v-for="item in method.items"
            :key="item.text"
            :to="item.link"
            class="group block p-3 sm:p-4 rounded-lg border hover:shadow-md transition-all duration-200 hover:border-primary/50"
          >
            <div class="flex items-center gap-2 sm:gap-3">
              <img
                :src="item.image"
                :alt="item.text"
                class="w-10 h-10 sm:w-12 sm:h-12 object-cover rounded-lg flex-shrink-0"
              />
              <div class="flex-1 min-w-0">
                <p class="text-xs sm:text-sm font-medium text-foreground group-hover:text-primary transition-colors">
                  {{ item.text }}
                </p>
              </div>
            </div>
          </RouterLink>
        </div>
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
  items: {
    text: string;
    image: string;
    link: string;
  }[];
}

defineProps<{
  method: MethodItem;
}>();
</script>
