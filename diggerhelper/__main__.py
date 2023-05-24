from argparse import ArgumentParser
from diggerhelper.tools import Query, Export


def setup_query_parser(parser_query: ArgumentParser):
    subparser_query = parser_query.add_subparsers(required=True)
    parser_query_repo = subparser_query.add_parser("repo", help="Query info about a certain repository")
    parser_query_repo.add_argument("-n", "--name", metavar="NAME", required=True, help="The name of the repository")
    parser_query_repo.add_argument("--metric", metavar="METRIC", required=True, help="The metric of query")
    parser_query_repo.add_argument("--time", metavar="TIME", default="*", help="Category result based on time")
    parser_query_repo.set_defaults(func=Query.repo)

    parser_query_user = subparser_query.add_parser("user", help="Query info about a certain user")
    parser_query_user.add_argument("-n", "--name", metavar="NAME", required=True, help="The name of the user")
    parser_query_user.add_argument("--metric", metavar="METRIC", required=True, help="The metric of query")
    parser_query_user.add_argument("--time", metavar="TIME", default="*", help="Category result based on time")
    parser_query_user.set_defaults(func=Query.user)


def setup_export_parser(parser_export: ArgumentParser):
    subparser_export = parser_export.add_subparsers(required=True)
    parser_export_file = subparser_export.add_parser("download", help="Download info into file")
    parser_export_file.add_argument("--query", metavar="repo/user", required=True, choices=['repo', 'user'], help="The type of query")
    parser_export_file.add_argument("-n", "--name", metavar="NAME", required=True, help="The name of the repo/user")
    parser_export_file.add_argument("--metric", metavar="METRIC", required=True, help="The metric of query")
    parser_export_file.add_argument("--time", metavar="TIME", default="*", help="Category result based on time")
    parser_export_file.add_argument("--type", metavar="json/pdf/jpg/png", default="json", choices=['json', 'pdf', 'jpg', 'png'], help="The type of output file")
    parser_export_file.add_argument("-o", "--output", metavar="PATH", default="./", help="The path of output file")
    parser_export_file.set_defaults(func=Export.download)

    parser_export_file = subparser_export.add_parser("web", help="Show info in web page")
    parser_export_file.add_argument("--query", metavar="repo/user", required=True, choices=['repo', 'user'],
                                    help="The type of query")
    parser_export_file.add_argument("-n", "--name", metavar="NAME", required=True, help="The name of the repo/user")
    parser_export_file.add_argument("--metric", metavar="METRIC", required=True, help="The metric of query")
    parser_export_file.add_argument("--time", metavar="TIME", default="*", help="Category result based on time")
    parser_export_file.set_defaults(func=Export.web)


def setup_parser():
    parser_main = ArgumentParser()
    subparsers_main = parser_main.add_subparsers(required=True)
    parser_query = subparsers_main.add_parser("query")
    setup_query_parser(parser_query)
    parser_export = subparsers_main.add_parser("export")
    setup_export_parser(parser_export)
    return parser_main


if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args()
    args.func(args)
