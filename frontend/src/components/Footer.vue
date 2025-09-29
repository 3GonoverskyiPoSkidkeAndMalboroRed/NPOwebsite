<script setup lang="ts">
import { ChevronsDown } from "lucide-vue-next";
import Separator from "./ui/separator/Separator.vue";
</script>

<template>
  <footer
    id="footer"
    class="container py-24 pb-16 sm:py-32 sm:pb-24"
  >
    <div class="p-10 bg-muted/50 dark:bg-card border rounded-2xl">
      <div
        class="grid grid-cols-1 lg:grid-cols-4 gap-x-12 gap-y-8"
      >
        <div class="col-span-1">
          <a
            href="#"
            class="flex font-bold items-center"
          >
            <ChevronsDown
              class="bg-gradient-to-tr from-primary via-primary/70 to-primary rounded-lg w-9 h-9 mr-2 border text-white"
            />

            <h3 class="text-2xl">НПО "СПЕКТРОН"</h3>
          </a>
        </div>

        <div class="col-span-1 lg:col-span-3 flex flex-col gap-2">
          <h3 class="font-bold text-lg">Контакты</h3>
          <div class="space-y-2">
            <div class="opacity-60">
              <p class="font-medium">ООО «НПО «СПЕКТРОН»</p>
              <p>Россия, 190020,</p>
              <p>Санкт-Петербург ул. Циолковcкого, д.10а</p>
            </div>
            
            <div class="space-y-1">
              <div>
                <span class="font-medium">Тел.:</span>
                <a href="tel:+78123258183" class="opacity-60 hover:opacity-100 ml-1">
                  (812) 325-8183
                </a>
              </div>
              
              <div>
                <span class="font-medium">Факс:</span>
                <span class="opacity-60 ml-1">(812) 325-8503</span>
              </div>
            </div>
            
            <div class="space-y-1">
              <div>
                <span class="font-medium">По общим вопросам:</span>
                <a href="mailto:info@spectronxray.ru" class="opacity-60 hover:opacity-100 ml-1">
                  info@spectronxray.ru
                </a>
              </div>
              
              <div>
                <span class="font-medium">Отдел продаж:</span>
                <a href="mailto:rus@spectronxray.ru" class="opacity-60 hover:opacity-100 ml-1">
                  rus@spectronxray.ru
                </a>
              </div>
              
              <div>
                <span class="font-medium">Отдел сервиса:</span>
                <a href="mailto:service@spectronxray.ru" class="opacity-60 hover:opacity-100 ml-1">
                  service@spectronxray.ru
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- platforms -->
        <!-- <div class="flex flex-col gap-2">
          <h3 class="font-bold text-lg">Platforms</h3>
          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              iOS
            </a>
          </div>

          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              Android
            </a>
          </div>

          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              Web
            </a>
          </div>
        </div> -->
        <!-- help -->
        <!-- <div class="flex flex-col gap-2">
          <h3 class="font-bold text-lg">Help</h3>
          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              Contact Us
            </a>
          </div>

          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              FAQ
            </a>
          </div>

          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              Feedback
            </a>
          </div>
        </div> -->
        <!-- socials -->
        <!-- <div class="flex flex-col gap-2">
          <h3 class="font-bold text-lg">Socials</h3>
          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              Twitch
            </a>
          </div>

          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              Discord
            </a>
          </div>

          <div>
            <a
              href="#"
              class="opacity-60 hover:opacity-100"
            >
              Dribbble
            </a>
          </div>
        </div> -->
      
      </div>

      <Separator class="my-6" />
      <section class="space-y-2">
        <p class="text-sm opacity-60 text-center">
          Информация на сайте не является публичной офертой
        </p>
        <h3 class="text-center">
          &copy; 2024 Designed and developed by
          <a
            target="_blank"
            href="https://github.com/leoMirandaa"
            class="text-primary transition-all border-primary hover:border-b-2"
          >
            Leo Miranda
          </a>
        </h3>
      </section>
    </div>
  </footer>
</template>
