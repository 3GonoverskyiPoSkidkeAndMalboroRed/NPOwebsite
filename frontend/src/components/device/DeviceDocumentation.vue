<template>
  <div v-if="activeTab === 'documentation'" class="space-y-6">
    <h3 class="text-2xl font-bold mb-4">Документация</h3>
    <div class="grid md:grid-cols-2 gap-6">
      <div v-for="doc in documentation" :key="doc.name" class="p-4 border rounded-lg hover:bg-muted/50 transition-colors">
        <div class="flex items-center gap-3">
          <div class="text-2xl">{{ doc.icon }}</div>
          <div class="flex-1">
            <h4 class="font-semibold">{{ doc.name }}</h4>
            <p class="text-sm text-muted-foreground">{{ doc.description }}</p>
          </div>
          <Button variant="outline" size="sm">
            Скачать
          </Button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";

interface Documentation {
  name: string;
  description: string;
  icon: string;
}

interface Props {
  activeTab: string;
  documentation: Documentation[];
}

defineProps<Props>();
</script>
