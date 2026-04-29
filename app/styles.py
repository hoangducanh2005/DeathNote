DEATHNOTE_CSS = """
<style>
    body {
        background:
            linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)),
            url('/res/light-yagami-black-anime-2zplmoceytxd85kl.jpg') center/cover no-repeat fixed;
        color: #e8dcc0;
    }

    .death-title {
        font-size: 52px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #c1121f;
        text-shadow: 0 0 8px #7a0000, 0 0 20px #000000;
    }

    .death-subtitle {
        color: #b8a77a;
        letter-spacing: 2px;
    }

    .main-book {
        background: linear-gradient(145deg, #111111, #050505);
        border: 1px solid #4a0000;
        box-shadow: 0 0 30px rgba(120, 0, 0, 0.35);
    }

    .rule-box {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid #8b0000;
    }

    .note-card {
        background:
            linear-gradient(135deg, rgba(30, 30, 30, 0.98), rgba(5, 5, 5, 0.98));
        border: 1px solid #5c0000;
        box-shadow: 0 0 14px rgba(120, 0, 0, 0.25);
        transition: 0.2s ease;
    }

    .note-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 22px rgba(180, 0, 0, 0.35);
    }

    .empty-card {
        background: rgba(0, 0, 0, 0.55);
        border: 1px dashed #5c0000;
    }

    .page-title {
        color: #d4af37;
        font-weight: bold;
        letter-spacing: 2px;
        font-size: 13px;
    }

    .note-content {
        color: #f2ead3;
        font-size: 18px;
        line-height: 1.7;
        white-space: pre-wrap;
    }

    .death-input textarea {
        color: #f2ead3 !important;
        caret-color: #c1121f !important;
    }

    .death-input .q-field__control {
        background: rgba(255, 255, 255, 0.04) !important;
    }

    .death-input .q-field__label {
        color: #b8a77a !important;
    }
</style>
"""