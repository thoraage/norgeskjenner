<script>
    import Geometry from "./geometry.svelte";
    import Quiz from "./quiz.svelte";
</script>

<style>
    :global(.map) {
        position:absolute;
        top: 0px;
        left: 15%;
        right: 15%;
        width: 70%;
        height: 100%;
    }

    :global(.map path) {
        fill-opacity: 0.25;
        stroke: black;
    }

    :global(.map path:first-child) {
        fill-opacity: 1;
    }
</style>

<Quiz />
<Geometry />
