<script>
    import {onMount} from "svelte";
    import Logo from './Logo.svelte'
    import DateDisplay from "./DateDisplay.svelte";
    import Calendar from "./Calendar.svelte";
    import Form from "./Form.svelte";

    const endpoint = process.env.NODE_ENV === 'development' ? 'http://localhost:5001' : 'https://dateparser-demo.herokuapp.com/'
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

    let date = new Date()
    let interval = null
    let error = null

    onMount(() => {
        interval = setInterval(() => date = new Date(), 1000)
    })

    const handleSubmit = async (event) => {
        error = null
        clearInterval(interval)

        let url = `${endpoint}?text=${encodeURI(event.detail.text)}`;
        if (timezone) {
            url += `&timezone=${timezone}`;
        }
        const response = await fetch(url);

        if (response.ok) {
            const dateText = await response.text()
            date = new Date(dateText)
        } else {
            error = 'Dateparser was not able to parse date'
        }
    };
</script>

<main>
    <section>
        <Logo/>
        <Form on:submit={handleSubmit} bind:error />
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

    @media (min-width: 600px) {
        main {
            margin-top: 156px;
        }
    }

    section {
        flex-basis: 50%;
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
    }
</style>
