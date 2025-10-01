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
    id: 'CLSW',
    name: 'СПЕКТРОСКАН CLSW',
    description: 'Анализатор хлора и серы',
    image: '/analyzers/CLSW/CLSW_1.jpg',
    route: '/analyzers/clsw'
  },
  {
    id: 'SE',
    name: 'СПЕКТРОСКАН SE',
    description: 'Анализатор серы',
    image: '/analyzers/SE/SE_1.jpg',
    route: '/analyzers/se'
  },
  {
    id: 'IS-T',
    name: 'СПЕКТРОСКАН IS-T',
    description: 'Анализатор серы поточный',
    image: '/analyzers/IS-T/IS-T_1.jpg',
    route: '/analyzers/is-t'
  },
  {
    id: 'MSW',
    name: 'СПЕКТРОСКАН MSW',
    description: 'Анализатор серы и металлов',
    image: '/analyzers/MSW.jpg',
    route: '/analyzers/msw'
  },
  {
    id: 'META',
    name: 'СПЕКТРОСКАН МЕТА',
    description: 'Анализатор серы и азота',
    image: '/analyzers/META/META_1.jpg',
    route: '/analyzers/meta'
  },
  {
    id: 'GVM',
    name: 'СПЕКТРОСКАН МАКС-GVM',
    description: 'Вакуумный волнодисперсионный рентгенофлуоресцентный спектрометр',
    image: '/spectrometrs/GVM/GVM_1.jpg',
    route: '/spectrometers'
  },
  {
    id: 'MAX-G',
    name: 'СПЕКТРОСКАН МАКС-G',
    description: 'Рентгенофлуоресцентный спектрометр',
    image: '/spectrometrs/МАКС-G/МАКС-G_1.jpg',
    route: '/spectrometers'
  },
  {
    id: 'MAX-GF1',
    name: 'СПЕКТРОСКАН МАКС-GF1(2)E',
    description: 'Рентгенофлуоресцентный спектрометр с газовым потоком',
    image: '/spectrometrs/МАКС-GF1(2)E/МАКС-GF1(2)E_1.jpg',
    route: '/spectrometers'
  },
  {
    id: 'MAX-GF1-C',
    name: 'СПЕКТРОСКАН МАКС-GF1(2)E-С',
    description: 'Рентгенофлуоресцентный спектрометр с газовым потоком (модификация С)',
    image: '/spectrometrs/МАКС-GF1(2)E-С/МАКС-GF1(2)E-С_1.png',
    route: '/spectrometers'
  },
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
