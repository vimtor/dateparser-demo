<script>
    export let date = new Date()
    import formatDate from 'dateformat'

    const prefers24TimeFormat = !new Intl.DateTimeFormat(navigator.language, {hour: "numeric"}).format(0).match(/AM/);
</script>

<div>
    <h2>
        {formatDate(date, `${prefers24TimeFormat ? "HH" : 'hh' }:MM:ss`)}
        <span class="period">
            {#if !prefers24TimeFormat}
                {formatDate(date, 'TT')}
            {/if}
        </span>
    </h2>
    <p>{formatDate(date, 'dddd, mmmm dd, yyyy')}</p>
    <span class="timezone">{formatDate(date, 'Z')}</span>
</div>

<style>
    div {
        text-align: center;
        margin: 4rem 0;
    }

    h2 {
        font-size: 2rem;
        margin: 0;
    }

    p {
        font-size: 1rem;
        margin: 1em 0 0;
    }

    .timezone {
        display: block;
        font-size: 0.9rem;
        margin-top: 0.5em;
        color: darkgray;
    }

    .period {
        font-weight: 400;
        font-size: 1.25rem;
        color: darkgray;
    }
</style>
