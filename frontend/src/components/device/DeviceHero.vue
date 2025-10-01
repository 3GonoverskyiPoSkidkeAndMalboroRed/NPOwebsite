<template>
  <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
    <div class="max-w-7xl mx-auto">
      <div class="grid lg:grid-cols-2 gap-12 items-center mb-16">
        <div>
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
            {{ title }}
          </h1>
          <p class="text-xl text-muted-foreground mb-8">
            {{ description }}
          </p>
          <div class="flex flex-col sm:flex-row gap-4">
            <Button size="lg" class="px-8">
              Получить консультацию
            </Button>
            <Button variant="outline" size="lg" class="px-8">
              Скачать каталог
            </Button>
          </div>
        </div>
        <div class="relative">
          <img 
            :src="mainImage" 
            :alt="title" 
            class="w-full h-auto rounded-lg shadow-lg cursor-pointer hover:opacity-90 transition-opacity"
            @click="openImageModal(0)"
          />
          
          <!-- Миниатюры всех изображений -->
          <div v-if="images.length > 1" class="flex gap-2 mt-4 justify-center">
            <img 
              v-for="(image, index) in images" 
              :key="index"
              :src="image" 
              :alt="`${title} - изображение ${index + 1}`"
              class="w-16 h-16 object-cover rounded cursor-pointer hover:opacity-70 transition-opacity border-2 border-transparent hover:border-primary"
              :class="{ 'border-primary': index === 0 }"
              @click="openImageModal(index)"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";

interface Props {
  title: string;
  description: string;
  mainImage: string;
  images: string[];
}

defineProps<Props>();

const emit = defineEmits<{
  openImageModal: [index: number];
}>();

const openImageModal = (index: number) => {
  emit('openImageModal', index);
};
</script>