<template>
  <div class="text-center bg-primary/10 rounded-lg p-8 border border-primary/20">
    <h3 class="text-2xl font-semibold mb-4">{{ title }}</h3>
    <p class="text-muted-foreground mb-6 max-w-2xl mx-auto">
      {{ description }}
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <Button size="lg" class="px-8">
        Получить консультацию
      </Button>
      <Button variant="outline" size="lg" class="px-8">
        Запросить коммерческое предложение
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";

interface Props {
  title: string;
  description: string;
}

defineProps<Props>();
</script>
