<script lang="ts">
    import municipalities from '$lib/municipalities.json';

    export let municipality;

    enum Result {
        WIN, LOSS, UNDECIDED
    }

    let result: Result = Result.UNDECIDED;

    let name = "";
    let error = "";
    let filteredMunicipalties = [];
    let tried: Array[String] = [];
    function filterMunicipalties() {
        if (name.length === 0) {
            filteredMunicipalties = [];
            return;
        }
        filteredMunicipalties = Object.values(municipalities).toSorted().filter((municipality) => {
            return municipality.toLowerCase().startsWith(name.toLowerCase());
        });
    }
    function submit(submittedName) {
        submittedName = submittedName.trim();
        let matchingMunicipalities = Object.values(municipalities)
            .filter(m => submittedName.trim().toLowerCase() === m.toLowerCase());
        if (municipality['name'] === submittedName) {
            result = Result.WIN;
        } else {
            if (tried.length < 3) {
                tried.push(submittedName);
                error = "Det var feil, prøv igjen!";
            } else {
                result = Result.LOSS;
            }
        }
    }
</script>

<div class="quiz">
    {#if result === Result.WIN}
        <p>Gratulerer, {municipality['name']} var riktig svar!</p>
    {:else if result === Result.LOSS}
        <p>Dessverre, du har svart feil! Riktig svar var {municipality['name']}</p>
    {:else if result === Result.UNDECIDED}
        <p>Hvilken kommune er dette</p>
        <form autocomplete="off" on:submit|preventDefault={submit(name)}>
            <input bind:value={name} placeholder="kommune" on:input={filterMunicipalties}/><br>
            <p>{error}</p>
        </form>
        {#if filteredMunicipalties.length > 0}
            <ul id="autocomplete-items-list">
                {#each filteredMunicipalties as municipality, i}
                    <li class="autocomplete-items" on:click={submit(municipality)}>{municipality}</li><!--class:autocomplete-active={highlighted}-->
                {/each}
            </ul>
        {/if}
    {/if}
</div>