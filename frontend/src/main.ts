import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import "./assets/index.css";

import Layout from "./views/Layout.vue";
import Home from "./views/Home.vue";
import Analyzers from "./views/Analyzers.vue";
import Spectrometers from "./views/Spectrometers.vue";
import ElementalAnalyzers from "./views/ElementalAnalyzers.vue";
import GasAnalyzers from "./views/GasAnalyzers.vue";
import MoistureAnalyzers from "./views/MoistureAnalyzers.vue";
import PhAnalyzers from "./views/PhAnalyzers.vue";
import ConductivityAnalyzers from "./views/ConductivityAnalyzers.vue";
import TurbidityAnalyzers from "./views/TurbidityAnalyzers.vue";
import Tasks from "./views/Tasks.vue";
import Profile from "./views/Profile.vue";
import Methods from "./views/Methods.vue";
import Company from "./views/Company.vue";
import Service from "./views/Service.vue";
import Certificates from "./views/Certificates.vue";
import Training from "./views/Training.vue";
import Regulations from "./views/Regulations.vue";
import RfaBasics from "./views/RfaBasics.vue";


// Страницы для методик
import MethodsExpert from "./views/methods/MethodsExpert.vue";
import MethodsOil from "./views/methods/MethodsOil.vue";
import MethodsEco from "./views/methods/MethodsEco.vue";
import MethodsMining from "./views/methods/MethodsMining.vue";
import MethodsMetallurgy from "./views/methods/MethodsMetallurgy.vue";
import MethodsDiagnostics from "./views/methods/MethodsDiagnostics.vue";
import MethodsGeology from "./views/methods/MethodsGeology.vue";
import MethodsResearch from "./views/methods/MethodsResearch.vue";
import MethodsGas from "./views/methods/MethodsGas.vue";

// Страницы для анализаторов
import SpectroscanMSW from "./views/analyzers/SpectroscanMSW.vue";
import SpectroscanSWD3 from "./views/analyzers/SpectroscanSWD3.vue";
import SpectroscanCLSW from "./views/analyzers/SpectroscanCLSW.vue";
import SpectroscanSE from "./views/analyzers/SpectroscanSE.vue";

// Страницы для спектрометров
import ICPMSSpectrometer from "./views/spectrometers/ICPMSSpectrometer.vue";
import FTIRSpectrometer from "./views/spectrometers/FTIRSpectrometer.vue";
import SpectroscanIST from "./views/analyzers/SpectroscanIST.vue";
import SpectroscanMETA from "./views/analyzers/SpectroscanMETA.vue";

const routes = [
  {
    path: "/",
    component: Layout,
    children: [
      {
        path: "",
        name: "Home",
        component: Home,
      },
      {
        path: "analyzers",
        name: "Analyzers",
        component: Analyzers,
      },
      {
        path: "spectrometers",
        name: "Spectrometers",
        component: Spectrometers,
      },
      {
        path: "analyzers/elemental",
        name: "ElementalAnalyzers",
        component: ElementalAnalyzers,
      },
      {
        path: "analyzers/gas",
        name: "GasAnalyzers",
        component: GasAnalyzers,
      },
      {
        path: "analyzers/moisture",
        name: "MoistureAnalyzers",
        component: MoistureAnalyzers,
      },
      {
        path: "analyzers/ph",
        name: "PhAnalyzers",
        component: PhAnalyzers,
      },
      {
        path: "analyzers/conductivity",
        name: "ConductivityAnalyzers",
        component: ConductivityAnalyzers,
      },
      {
        path: "analyzers/turbidity",
        name: "TurbidityAnalyzers",
        component: TurbidityAnalyzers,
      },
      {
        path: "tasks",
        name: "Tasks",
        component: Tasks,
      },
      {
        path: "profile",
        name: "Profile",
        component: Profile,
      },
      {
        path: "methods",
        name: "Methods",
        component: Methods,
      },
      {
        path: "company",
        name: "Company",
        component: Company,
      },
      {
        path: "service",
        name: "Service",
        component: Service,
      },
      {
        path: "certificates",
        name: "Certificates",
        component: Certificates,
      },
      {
        path: "training",
        name: "Training",
        component: Training,
      },
      {
        path: "regulations",
        name: "Regulations",
        component: Regulations,
      },
      {
        path: "rfa-basics",
        name: "RfaBasics",
        component: RfaBasics,
      },
      {
        path: "methods-expert",
        name: "MethodsExpert",
        component: MethodsExpert,
      },
      {
        path: "methods-oil",
        name: "MethodsOil",
        component: MethodsOil,
      },
      {
        path: "methods-eco",
        name: "MethodsEco",
        component: MethodsEco,
      },
      {
        path: "methods-mining",
        name: "MethodsMining",
        component: MethodsMining,
      },
      {
        path: "methods-metallurgy",
        name: "MethodsMetallurgy",
        component: MethodsMetallurgy,
      },
      {
        path: "methods-diagnostics",
        name: "MethodsDiagnostics",
        component: MethodsDiagnostics,
      },
      {
        path: "methods-geology",
        name: "MethodsGeology",
        component: MethodsGeology,
      },
      {
        path: "methods-research",
        name: "MethodsResearch",
        component: MethodsResearch,
      },
      {
        path: "methods-gas",
        name: "MethodsGas",
        component: MethodsGas,
      },
      {
        path: "analyzers/msw",
        name: "SpectroscanMSW",
        component: SpectroscanMSW,
      },
      {
        path: "analyzers/sw-d3",
        name: "SpectroscanSWD3",
        component: SpectroscanSWD3,
      },
      {
        path: "analyzers/clsw",
        name: "SpectroscanCLSW",
        component: SpectroscanCLSW,
      },
      {
        path: "analyzers/se",
        name: "SpectroscanSE",
        component: SpectroscanSE,
      },
      {
        path: "analyzers/is-t",
        name: "SpectroscanIST",
        component: SpectroscanIST,
      },
      {
        path: "analyzers/meta",
        name: "SpectroscanMETA",
        component: SpectroscanMETA,
      },
      {
        path: "spectrometers/icp-ms",
        name: "ICPMSSpectrometer",
        component: ICPMSSpectrometer,
      },
      {
        path: "spectrometers/ftir",
        name: "FTIRSpectrometer",
        component: FTIRSpectrometer,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Guard для защиты маршрутов - защищаем только /profile
router.beforeEach(async (to, _from, next) => {
  // Проверяем, является ли маршрут защищенным (только /profile)
  if (to.path === '/profile') {
    // Проверяем авторизацию только для страницы профиля
    const token = localStorage.getItem('token');
    if (!token) {
      // Если токена нет, разрешаем доступ к /profile (покажет форму авторизации)
      next();
      return;
    }
    
    // Проверяем валидность токена
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/auth/me`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      
      if (!response.ok) {
        // Токен недействителен, удаляем его, но разрешаем доступ к /profile
        localStorage.removeItem('token');
      }
    } catch (error) {
      // Ошибка сети, удаляем токен, но разрешаем доступ к /profile
      localStorage.removeItem('token');
    }
  }
  
  // Для всех остальных маршрутов разрешаем доступ без проверки
  next();
});

const app = createApp(App);
app.use(router);
app.mount("#app");
