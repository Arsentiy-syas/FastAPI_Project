let loadingPromise = null;

export function loadYandexMaps() {
  if (window.ymaps3) {
    return Promise.resolve(window.ymaps3);
  }

  if (!loadingPromise) {
    loadingPromise = new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src =
        "https://api-maps.yandex.ru/v3/?apikey=fcc4cabf-e4ff-4765-8915-ece327999016&lang=ru_RU";
      script.async = true;

      script.onload = () => resolve(window.ymaps3);
      script.onerror = reject;

      document.head.appendChild(script);
    });
  }

  return loadingPromise;
}
