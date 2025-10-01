<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

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
  <section id="hero" class="container px-4 sm:px-6 lg:px-8">
    <div
      class="grid place-items-center lg:max-w-screen-xl gap-4 sm:gap-6 lg:gap-8 mx-auto py-8 sm:py-12 md:py-16 lg:py-24 xl:py-32"
    >
      <div class="text-center space-y-4 sm:space-y-6 lg:space-y-8">
        <div
          class="max-w-screen-md mx-auto text-center text-2xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl font-bold"
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
      <div class="relative group mt-6 sm:mt-8 lg:mt-12 w-full max-w-6xl mx-auto overflow-hidden">
        <!-- gradient shadow -->
        <div
          class="absolute -top-2 sm:-top-4 lg:-top-6 right-2 sm:right-4 lg:right-12 w-[60%] sm:w-[70%] lg:w-[50%] h-6 sm:h-8 lg:h-12 xl:h-[30%] bg-primary/50 blur-3xl rounded-full img-shadow-animation"
        ></div>

        <Carousel class="w-full">
          <CarouselContent class="-ml-1 sm:-ml-2 md:-ml-4">
            <CarouselItem 
              v-for="instrument in instruments" 
              :key="instrument.id"
              class="pl-1 sm:pl-2 md:pl-4"
            >
              <div class="flex flex-col lg:flex-row gap-3 sm:gap-4 h-auto lg:h-96">
                <!-- Левая часть - Изображение -->
                <div 
                  class="flex-3 rounded-lg border-2 bg-white overflow-hidden cursor-pointer hover:shadow-lg transition-shadow h-72 sm:h-48 md:h-56 lg:h-auto"
                  @click="navigateToInstrument(instrument.route)"
                >
                  <div class="relative h-full">
                    <img
                      :src="instrument.image"
                      :alt="instrument.name"
                      class="w-full h-full object-cover"
                    />
                    <!-- Легкий оверлей для лучшей читаемости -->
                    <div class="absolute inset-0 bg-black/10"></div>
                  </div>
                </div>
                <!-- Правая часть - Текстовый блок -->
                <div 
                  class="flex-1 rounded-lg p-3 sm:p-4 lg:p-6 flex flex-col justify-center cursor-pointer hover:shadow-lg transition-shadow"
                  @click="navigateToInstrument(instrument.route)"
                >
                  <h3 class="text-lg sm:text-xl lg:text-2xl xl:text-3xl font-bold mb-2 sm:mb-3 lg:mb-4">
                    {{ instrument.name }}
                  </h3>
                  <p class="text-sm sm:text-base lg:text-lg mb-3 sm:mb-4 lg:mb-6">
                    {{ instrument.description }}
                  </p>
                </div>
              </div>
            </CarouselItem>
          </CarouselContent>
          
          <!-- Навигационные кнопки для ПК (снизу) -->
          <CarouselPrevious class="carousel-buttons hidden md:flex left-1/2 transform -translate-x-1/2 -translate-x-8 sm:-translate-x-12 md:-translate-x-16 top-full mt-4 sm:mt-6 lg:mt-8 bg-black/70 hover:bg-black/80 text-white border-white/50 shadow-lg w-8 h-8 sm:w-10 sm:h-10" />
          <CarouselNext class="carousel-buttons hidden md:flex left-1/2 transform -translate-x-1/2 translate-x-8 sm:translate-x-12 md:translate-x-16 top-full mt-4 sm:mt-6 lg:mt-8 bg-black/70 hover:bg-black/80 text-white border-white/50 shadow-lg w-8 h-8 sm:w-10 sm:h-10" />
          
          <!-- Дополнительные кнопки навигации по бокам для ПК -->
          <CarouselPrevious class="carousel-buttons hidden lg:flex absolute left-4 top-1/2 transform -translate-y-1/2 bg-white/90 hover:bg-white text-black border-gray-300 shadow-lg w-10 h-10 z-10" />
          <CarouselNext class="carousel-buttons hidden lg:flex absolute right-4 top-1/2 transform -translate-y-1/2 bg-white/90 hover:bg-white text-black border-gray-300 shadow-lg w-10 h-10 z-10" />
        </Carousel>
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
    opacity: 0.1;
    transform: translateY(170px);
  }

  to {
    opacity: 1;
    transform: translateY(150px);
  }
}
@keyframes img-border-animation {
  from {
    border-top-color: rgb(var(--primary) / 0.1);
  }

  to {
    border-top-color: rgb(var(--primary) / 0.6);
  }
}

/* Дополнительные стили для адаптивности */
@media (max-width: 640px) {
  .container {
    overflow-x: hidden;
  }
}

/* Обеспечиваем, что кнопки карусели не выходят за границы */
@media (max-width: 480px) {
  .carousel-buttons {
    transform: scale(0.8);
  }
}

/* Дополнительная защита для очень маленьких экранов */
@media (max-width: 360px) {
  .carousel-buttons {
    transform: scale(0.7);
  }
  
  .container {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }
}
</style>
