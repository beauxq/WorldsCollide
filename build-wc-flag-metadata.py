def main() -> None:
    from WorldsCollide import args
    from WorldsCollide.metadata.flag_metadata_writer import FlagMetadataWriter
    FlagMetadataWriter(args).write()


if __name__ == '__main__':
    main()
