<template>
  <div class="min-h-screen bg-background">
    <section class="py-20 px-4">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text text-transparent">
            Кондуктометры
          </h1>
          <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
            Измерение электропроводности растворов и жидкостей
          </p>
        </div>
        
        <div class="text-center">
          <p class="text-lg text-muted-foreground mb-8">
            Страница находится в разработке
          </p>
          <Button @click="$router.push('/analyzers')" variant="outline">
            ← Вернуться к анализаторам
          </Button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";
</script>
