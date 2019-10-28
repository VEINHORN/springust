# springust

Command line tool which simplifies day-to-day work with Spring.

## Installation

### Fish

Add alias to your **fish** shell:

```fish
alias sg='~/github/springust/scripts/springust.sh'
```

## Commands

### Generate

There are a bunch of commands available in **springust** CLI.

#### Controller

To generate new controller just type below command:

```shell
springust generate controller <controller_name> --crud
```

You can use 

#### Domain

You can generate domain. Domain it's common name for entity/DTO/mapping.

Example:

Below example will create 3 classes: UserEntity, UserDto and UserMapper (based on MapStruct library).

```shell
springust generate domain user
```
