<script>
    import {onMount} from "svelte";
    import Logo from './Logo.svelte'
    import DateDisplay from "./DateDisplay.svelte";
    import Calendar from "./Calendar.svelte";
    import Form from "./Form.svelte";

    const endpoint = process.env.NODE_ENV === 'development' ? 'http://localhost:5001' : 'https://dateparser-demo-production.up.railway.app/'
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
    <footer class="copyright">
        Powered by <a href="https://github.com/scrapinghub/dateparser">Dateparser</a> Python library
        <br />
        <br />
        Built with ❤ by <a href="https://vimtor.io">Victor Navarro</a> in Twitch
    </footer>
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
        max-width: 50rem;
        margin-left: auto;
        margin-right: auto;
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

    .copyright {
        margin-top: 64px;
    }
</style>
