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
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <RouterLink
            v-for="item in method.items"
            :key="item.text"
            :to="item.link"
            class="group block p-4 rounded-lg border hover:shadow-md transition-all duration-200 hover:border-primary/50"
          >
            <div class="flex items-center gap-3">
              <img
                :src="item.image"
                :alt="item.text"
                class="w-12 h-12 object-cover rounded-lg flex-shrink-0"
              />
              <div class="flex-1 min-w-0">
                <p class="text-sm font-medium text-foreground group-hover:text-primary transition-colors">
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
  description: string;
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
