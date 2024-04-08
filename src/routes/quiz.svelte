<script>
    import municipalities from '$lib/municipalities.json';

    let name = "";
    let filteredMunicipalties = [];
    let tries = 0;
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
        console.log("Submit: " + submittedName);
        let matchingMunicipalities = Object.values(municipalities).filter(m => submittedName.toLowerCase() === m.toLowerCase());
        if (matchingMunicipalities.length > 0) {
            console.log("Found");
        } else {
            console.log("Incorrect");
        }
    }
</script>

<div class="quiz">
    <p>Hvilken kommune er dette</p>
    <form autocomplete="off" on:submit|preventDefault={submit(name)}>
        <input bind:value={name} placeholder="kommune" on:input={filterMunicipalties}/>
    </form>
    {#if filteredMunicipalties.length > 0}
        <ul id="autocomplete-items-list">
            {#each filteredMunicipalties as municipality, i}
                <li class="autocomplete-items" on:click={submit(municipality)}>{municipality}</li><!--class:autocomplete-active={highlighted}-->
            {/each}
        </ul>
    {/if}
</div>