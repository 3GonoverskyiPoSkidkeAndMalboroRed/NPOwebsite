<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-vue-next";
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from "@/components/ui/carousel";

// Данные о приборах
const instruments = ref([
  {
    id: 'conductivity',
    name: 'Кондуктометры',
    description: 'Измерение электропроводности растворов и жидкостей',
    image: 'spectroscan-msw.jpg',
    route: '/analyzers'
  },
  {
    id: 'ph',
    name: 'pH-метры',
    description: 'Измерение кислотности и щелочности растворов',
    image: 'spectroscan-msw.jpg',
    route: '/ph-analyzers'
  },
  {
    id: 'turbidity',
    name: 'Турбидиметры',
    description: 'Измерение мутности и прозрачности жидкостей',
    image: 'spectroscan-msw.jpg',
    route: '/turbidity-analyzers'
  },
  {
    id: 'elemental',
    name: 'Элементные анализаторы',
    description: 'Анализ элементного состава веществ',
    image: 'spectroscan-msw.jpg',
    route: '/elemental-analyzers'
  },
  {
    id: 'gas',
    name: 'Газовые анализаторы',
    description: 'Анализ газового состава и концентраций',
    image: 'hero-image-light.jpg',
    route: '/gas-analyzers'
  },
  {
    id: 'moisture',
    name: 'Влагомеры',
    description: 'Измерение влажности материалов и веществ',
    image: 'hero-image-dark.jpg',
    route: '/moisture-analyzers'
  }
]);

const navigateToInstrument = (route: string) => {
  router.push(route);
};
</script>

<template>
  <section id="hero" class="container">
    <div
      class="grid place-items-center lg:max-w-screen-xl gap-8 mx-auto py-20 md:py-32"
    >
      <div class="text-center space-y-8">
        <div
          class="max-w-screen-md mx-auto text-center text-5xl md:text-6xl font-bold"
        >
          <h1>
           
            <span
              class="text-transparent bg-gradient-to-r from-[#D247BF] to-primary bg-clip-text"
              >Приборы
            </span>
            которые мы производим
          </h1>
        </div>


        
      </div>

      <!-- Карусель с приборами -->
      <div class="relative group mt-14 w-full max-w-6xl mx-auto">
        <!-- gradient shadow -->
        <div
          class="absolute -top-6 right-12 w-[90%] h-12 lg:h-[80%] bg-primary/50 blur-3xl rounded-full img-shadow-animation"
        ></div>

        <Carousel class="w-full">
          <CarouselContent class="-ml-2 md:-ml-4">
            <CarouselItem 
              v-for="instrument in instruments" 
              :key="instrument.id"
              class="pl-2 md:pl-4"
            >
              <div class="relative group/card">
                <!-- Карточка прибора -->
                <div 
                  class="relative overflow-hidden rounded-lg border border-t-2 border-t-primary/30 bg-card/50 backdrop-blur-sm cursor-pointer"
                  @click="navigateToInstrument(instrument.route)"
                >
                  <!-- Изображение прибора -->
                  <div class="relative h-64 md:h-80 overflow-hidden">
                    <img
                      :src="instrument.image"
                      :alt="instrument.name"
                      class="w-full h-full object-cover"
                    />
                    <!-- Градиентный оверлей -->
                    <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
                  </div>

                  <!-- Контент карточки -->
                  <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                    <h3 class="text-2xl md:text-3xl font-bold mb-2">
                      {{ instrument.name }}
                    </h3>
                    <p class="text-sm md:text-base text-white/90 mb-4">
                      {{ instrument.description }}
                    </p>
                    <Button 
                      variant="secondary" 
                      size="sm"
                      class="bg-white/20 hover:bg-white/30 text-white border-white/30"
                    >
                      Подробнее
                      <ArrowRight class="ml-2 h-4 w-4" />
                    </Button>
                  </div>
                </div>
              </div>
            </CarouselItem>
          </CarouselContent>
          
          <!-- Навигационные кнопки -->
          <CarouselPrevious class="left-4 bg-black/70 hover:bg-black/80 text-white border-white/50 shadow-lg" />
          <CarouselNext class="right-4 bg-black/70 hover:bg-black/80 text-white border-white/50 shadow-lg" />
        </Carousel>

        <!-- gradient effect -->
        <div
          class="absolute bottom-0 left-0 w-full h-20 md:h-28 bg-gradient-to-b from-background/0 via-background/50 to-background rounded-lg pointer-events-none"
        ></div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.img-shadow-animation {
  animation-name: img-shadow-animation;
  animation-iteration-count: infinite;
  animation-duration: 2s;
  animation-timing-function: linear;
  animation-direction: alternate;
}

.img-border-animation {
  animation-name: img-border-animation;
  animation-iteration-count: infinite;
  animation-duration: 2s;
  animation-timing-function: linear;
  animation-direction: alternate;
}

@keyframes img-shadow-animation {
  from {
    opacity: 0.5;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0px);
  }
}
@keyframes img-border-animation {
  from {
    @apply border-t-primary/10;
  }

  to {
    @apply border-t-primary/60;
  }
}
</style>
