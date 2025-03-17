# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.4.0] - 2025-03-17

### Added

- `docs/api/fetch_river_levels.py` script to pull river level snapshots and output them to a `snapshot.json` file for consumption by the application.

## [2.3.0] - 2024-09-16

### Changed

- Updated the static river data file to only show floats between 2022 and Present to limit the data load.
- "Gage Height Last Updated" label to "Range" when using a static CSV file to display the start and end date/time range.
- No longer displaying floats on the legend if they don't fall between the start and end date/time range when using static data.

### Fixed

- Duplicate X axis values.

## [2.2.3] - 2024-08-27

### Changed

- Misc. changes + change to a static website.

## [2.2.2] - 2024-08-18

### Removed

- Custom domain name from endpoint.

## [2.2.1] - 2024-06-26

### Fixed

- Fixed copyright footer and fun facts.

## [2.2.0] - 2024-05-31

### Added

- Last River Level to header.

### Fixed

- Fun Facts being cut off on mobile, increased height.

## [2.1.0] - 2024-05-29

### Added

- Fun River and Tubing facts on the loading screen.
- JavaScript and CSS to handle the Fun Facts `</div>` tag.
- 20 Fun Facts in the `static/data/fun_facts.json` file.
- Updated site timestamp title

## [2.0.0] - 2024-05-28

### Added

- The ability to use static data in the `snapshot.json` file, vs. making `API` calls (snapshot vs. live).
- `END_DATE` and `TIME_ZONE` configuration variables.
- `VERSION` file to sync releases between the repo and server.

### Changed

- The "Gage Height Last Updated" timestamp from the last date retrieved from the sample data vs. the current datetime.
- `README` to cover the above additions.

## [1.1.1] - 2024-04-28

### Fixed

- Wave animation not properly rendering on certain mobile devices (aspect ratios) (#2).

## [1.1.0] - 2023-11-23

### Changed

- Updated `README` and repo structure to conform to the [Personal Repository Guidelines (PRG)](https://github.com/scottgriv/PRG-Personal-Repository-Guidelines) system.

### Removed

- `VERSION` file.
 
## [1.0.0] - 2023-10-26

### Added

- Added this changelog file :D.
- Initial Release of River Charts.

[2.4.0]: https://github.com/scottgriv/River-Charts/compare/2.3.0..2.4.0
[2.3.0]: https://github.com/scottgriv/River-Charts/compare/v2.2.3..2.3.0
[2.2.3]: https://github.com/scottgriv/River-Charts/compare/v2.2.2..v2.2.3
[2.2.2]: https://github.com/scottgriv/River-Charts/compare/v2.2.1..v2.2.2
[2.2.1]: https://github.com/scottgriv/River-Charts/compare/v2.2.0..v2.2.1
[2.2.0]: https://github.com/scottgriv/River-Charts/compare/v2.1.0..v2.2.0
[2.1.0]: https://github.com/scottgriv/River-Charts/compare/v2.0.0..v2.1.0
[2.0.0]: https://github.com/scottgriv/River-Charts/compare/v1.1.1...v2.0.0
[1.1.1]: https://github.com/scottgriv/River-Charts/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/scottgriv/River-Charts/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/scottgriv/River-Charts/releases/tag/v1.0.0