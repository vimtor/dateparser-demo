<script>
    export let date = new Date()
    import formatDate from 'dateformat'

</script>

<div>
    <h2>{formatDate(date, 'HH:MM')}</h2>
    <p>{formatDate(date, 'dddd, mmmm dd, yyyy')}</p>
    <span>{formatDate(date, 'Z')}</span>
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

    span {
        display: block;
        font-size: 0.9rem;
        margin-top: 0.5em;
        color: darkgray;
    }
</style>
