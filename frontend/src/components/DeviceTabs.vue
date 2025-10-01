<template>
  <section class="py-20 px-4 bg-muted/30">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-12">
        <h2 class="text-3xl md:text-4xl font-bold mb-4">
          Подробная информация
        </h2>
      </div>

      <!-- Навигация по вкладкам -->
      <div class="flex flex-wrap justify-center gap-2 mb-12">
        <Button 
          v-for="tab in tabs" 
          :key="tab.id"
          :variant="activeTab === tab.id ? 'default' : 'outline'"
          @click="$emit('update:activeTab', tab.id)"
          class="min-w-[120px]"
        >
          {{ tab.label }}
        </Button>
      </div>

      <!-- Контент вкладок -->
      <div class="bg-background rounded-2xl p-8 shadow-sm">
        <slot :activeTab="activeTab" />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";

interface Tab {
  id: string;
  label: string;
}

interface Props {
  activeTab: string;
  tabs: Tab[];
}

defineProps<Props>();

defineEmits<{
  'update:activeTab': [value: string];
}>();
</script>
