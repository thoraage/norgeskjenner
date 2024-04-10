<script>
    import counties from '$lib/f.json';
    import norway from '$lib/norway.json';
    import {GeoJSON2SVG} from 'geojson2svg';

    export let municipality;
    const width = '100%', height = 900;

    function mapExtent() {
        function mostish(f, arr) {
            let most = arr[0];
            arr.forEach(e => most = f(most, e));
            return most;
        }

        let coordinates = counties.Fylke.features.map(f => f.geometry.coordinates.flat(2)).flat(1);
        let longs = coordinates.map(a => a[0]).flat(1);
        let lats = coordinates.map(a => a[1]).flat(1);
        console.log(lats);
        console.log(longs);
        return {
            left: mostish(Math.min, longs),
            bottom: mostish(Math.min, lats),
            right: mostish(Math.max, longs),
            top: mostish(Math.max, lats)
        }
    }

    const options = {viewportSize: {width: 900, height: height}, mapExtent: mapExtent()};
    const converter = new GeoJSON2SVG(options);
    const svgStrings = converter.convert(municipality.geometry) + converter.convert(norway);
    // let count = municipality.geometry.coordinates[0][0].length;
</script>

<div class="map">
    <svg {width} {height}>
        {@html svgStrings}
    </svg>
</div>