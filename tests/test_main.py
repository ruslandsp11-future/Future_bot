from future_bot.__main__ import build_parser


def test_parser_allows_timer_and_chat_polling_together():
    args = build_parser().parse_args(["--daemon", "--poll-chat"])

    assert args.daemon is True
    assert args.poll_chat is True
