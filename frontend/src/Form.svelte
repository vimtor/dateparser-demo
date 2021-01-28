<script>
    export let error = ''
    import {createEventDispatcher} from 'svelte'

    let value = ''
    const dispatch = createEventDispatcher()

    const handleSubmit = (event) => {
        event.preventDefault()
        dispatch('submit', {
            text: value,
        })
    }
</script>

<form on:submit={handleSubmit}>
    <label for="text">
        Enter a string and get the result from Dateparser:
    </label>
    <input id="text" placeholder="now" type="text" bind:value>
    <button>Submit</button>
    {#if error}
        <p class="error">{error}</p>
    {/if}
</form>

<style>
    form {
        margin-top: 2rem;
        text-align: center;
    }

    label {
        display: block;
        font-size: 0.75rem;
        margin-bottom: 1rem;
    }

    input {
        border-radius: 8px;
        border: 1px solid black;
        padding: 0.5em;
        outline: none;
    }

    button {
        border-radius: 8px;
        border: 1px solid hsl(358, 90%, 45%);
        padding: 0.5em 1em;
        background-color: hsl(358, 90%, 45%);
        cursor: pointer;
        color: white;
    }

    button:hover,
    button:focus {
        background-color: hsl(358, 90%, 40%);
        outline: none;
    }

    .error {
        color: hsl(358, 90%, 45%);
        font-size: 0.75rem;
    }
</style>
