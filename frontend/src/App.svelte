<script>
    import Logo from './Logo.svelte'
    import DateDisplay from "./DateDisplay.svelte";
    import Calendar from "./Calendar.svelte";

    const endpoint = 'http://localhost:5000';
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

    let date = new Date()
    let text = ''

    const handleSubmit = async event => {
        event.preventDefault()
        const url = `${endpoint}?text=${encodeURI(text)}&timezone=${timezone}`;
        const response = await fetch(url);
        if (response.ok) {
            const dateText = await response.text()
            date = new Date(dateText)
        } else {
            // TODO: Invalid date logic
        }
    };
</script>

<main>
    <section>
        <Logo/>
        <form on:submit={handleSubmit}>
            <input aria-label="dateparser demo text" placeholder="now" type="text" bind:value={text}>
            <button>Submit</button>
        </form>
            <DateDisplay bind:date/>
    </section>
    <section class="displays">
        <Calendar bind:date/>
    </section>
</main>

<style>
    * {
        box-sizing: border-box;
        font-family: 'Varela Round', sans-serif;
    }

    main {
        margin-top: 96px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
    }

    input {
        margin-top: 2rem;
        border-radius: 8px;
        border: 1px solid black;
        padding: 0.5em;
        outline: none;
    }

    button {
        border-radius: 8px;
        border: 1px solid black;
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

    section {
        flex-basis: 50%;
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
    }
</style>
