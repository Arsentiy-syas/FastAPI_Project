import { useEffect, useRef, useState } from "react";
import { loadYandexMaps } from "./loadYandexMaps";
import "./MapComponent.css";

const MapComponent = () => {
  const mapRef = useRef(null);
  const [popup, setPopup] = useState(null);

  useEffect(() => {
    const initMap = async () => {
      const ymaps3 = await loadYandexMaps();
      await ymaps3.ready;

      const {
        YMap,
        YMapDefaultSchemeLayer,
        YMapDefaultFeaturesLayer,
        YMapMarker,
      } = ymaps3;

      const map = new YMap(mapRef.current, {
        location: {
          center: [28.75, 60.7],
          zoom: 13,
        },
      });

      map.addChild(new YMapDefaultSchemeLayer());
      map.addChild(new YMapDefaultFeaturesLayer());

      const response = await fetch("http://localhost:8000/marker_cafe");
      const points = await response.json();

      points.forEach((point) => {
        const el = document.createElement("div");
        el.className = "map-marker";

        el.addEventListener("click", () => {
          setPopup(point);
        });

        map.addChild(
          new YMapMarker(
            { coordinates: [point.longitude, point.latitude] },
            el
          )
        );
      });
    };

    initMap();
  }, []);

  return (
    <>
      <div ref={mapRef} className="map-container" />
      {popup && (
        <div className="map-popup">
          <strong>{popup.title}</strong>
          <div>{popup.description}</div>
        </div>
      )}
    </>
  );
};

export default MapComponent;
