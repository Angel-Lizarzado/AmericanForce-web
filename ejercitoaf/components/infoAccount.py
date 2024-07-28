import reflex as rx
from ejercitoaf.state.userState import UserState


def infoAccount(time: dict) -> rx.Component:
    return rx.center(
            rx.hstack(
            rx.spacer(),
            rx.image(src=f"https://www.habbo.es/habbo-imaging/avatarimage?direction=2&head_direction=2&size=l&user={UserState.username}"),
            rx.spacer(),
            rx.vstack(
                rx.heading(f"{UserState.username}"),
                rx.text(f"{UserState.rank_name} [A.F] #{UserState.user_id}"),
                rx.cond(
                    time['status'] == "Iniciado",
                    rx.moment(
                        time['start_time'],
                        format="HH:mm:ss",
                        duration_from_now=True,
                        interval=1000,
                        tz="UTC"
                    ),
                    rx.text(f"Tiempo : {time['total_time']}"),
                ),
                rx.cond(
                    time['status'] == "Sin time",
                    rx.fragment(),
                    rx.cond(
                        time["timerBy"] != "",
                        rx.box(
                            rx.text("Time llevado por:"),
                            rx.badge(time["timerBy"], color_scheme="yellow", variant="surface"),   
                            overflow="hidden",
                            text_overflow="ellipsis",
                            white_space="nowrap",
                        ),
                        rx.fragment(),
                    ),

                ),
                rx.cond(
                    time['status'] == "Sin time",
                        rx.fragment(),
                        rx.cond(
                            time['status'] == "Iniciado",
                            rx.badge("Iniciado", color_scheme="green"),
                            rx.badge("Pausado", color_scheme="red")
                        ),
                ),
            ),
            rx.spacer(),
            rx.cond(
            (UserState.user_rank >= 1) & (UserState.user_rank <= 11),
            rx.vstack(
                rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09134s02044s01134s42014t500140557b5fa4b48290bdfff0b317faa6520.png", width="85px", height="auto", margin="auto"),
                rx.heading("INICIALES", color="red"),
                margin="auto"
            ),
            rx.cond(
                    (UserState.user_rank >= 12) & (UserState.user_rank <= 22),
                    rx.vstack(
                        rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09134s02120s01135s42014t5101410e34e10dde76dac34683d4dd422a940.png", width="85px", height="auto", margin="auto"),
                        rx.heading("INFANTERIA", color="red"),
                        margin="auto"
                    ),
                    rx.cond(
                        (UserState.user_rank >= 22) & (UserState.user_rank <= 31),
                        rx.vstack(
                            rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09134s02017s01134s42014t5201453c44c80aae8102726c2e48525d304ae.png", width="85px", height="auto", margin="auto"),
                            rx.heading("ARTILLERIA", color="red"),
                            margin="auto"
                        ),
                        rx.cond(
                            (UserState.user_rank >= 32) & (UserState.user_rank <= 41),
                            rx.vstack(
                                rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09134s02110s01130s42014t53014d6986560084b5c145861451cfb35f32c.png", width="85px", height="auto", margin="auto"),
                                rx.heading("MARINA", color="red"),
                                margin="auto"
                            ),
                            rx.cond(
                                (UserState.user_rank >= 42) & (UserState.user_rank <= 51),
                                rx.vstack(
                                    rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09134s02200s01130s42014t5401429a141bdd894bd6cc863a169ba75028f.png", width="85px", height="auto", margin="auto"),
                                    rx.heading("AIR FORCE", color="red"),
                                    margin="auto"
                                ),
                                rx.cond(
                                    (UserState.user_rank >= 52) & (UserState.user_rank <= 59),
                                    rx.vstack(
                                        rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09114s02061s42014s43114t271146488ad9679ad17a8f8cc14a71e2cd633.png", width="85px", height="auto", margin="auto"),
                                        rx.heading("BLINDADOS", color="red"),
                                        margin="auto"
                                    ),
                                    rx.cond(
                                    (UserState.user_rank >= 60) & (UserState.user_rank <= 68),
                                        rx.vstack(
                                            rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09114s02100s43114s42014t271147898f40245455a58cbf5fbb846553d86.png", width="85px", height="auto", margin="auto"),
                                            rx.heading("FUERZAS ARMADAS ESPECIALES", color="red"),
                                            margin="auto"
                                        ),
                                        rx.cond(
                                            (UserState.user_rank >= 69) & (UserState.user_rank <= 78),
                                            rx.vstack(
                                                rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09114s02084s43114s42014t27114caead1eb35b6dde61fa99a2ea2910e55.png", width="85px", height="auto", margin="auto"),
                                                rx.heading("ESPECIALISTAS", color="red"),
                                                margin="auto"
                                            ),
                                            rx.cond(
                                                (UserState.user_rank >= 79) & (UserState.user_rank <= 87),
                                                rx.vstack(
                                                    rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09114s02154s42014s43114t2711475a1f3b0f5c49c89f7d38e0335927832.png", width="85px", height="auto", margin="auto"),
                                                    rx.heading("HALCONES", color="red"),
                                                    margin="auto"
                                                ),
                                                rx.cond(
                                                    (UserState.user_rank >= 88) & (UserState.user_rank <= 97),
                                                    rx.vstack(
                                                        rx.image(src="https://www.habbo.es/habbo-imaging/badge/b07114s02190s43114s57194s5510069edfd59190ed4ed06b2a5b37e905cd3.png", width="85px", height="auto", margin="auto"),
                                                        rx.heading("IMPERIALES", color="red"),
                                                        margin="auto"
                                                    ),
                                                    rx.cond(
                                                        (UserState.user_rank >= 98) & (UserState.user_rank <= 109),
                                                        rx.vstack(
                                                            rx.image(src="https://www.habbo.es/habbo-imaging/badge/b17134s02244s03117t52011s34024b805f170102284ffd919788f08d3bbe3.png", width="85px", height="auto", margin="auto"),
                                                            rx.heading("REPUBLICA GALACTICA", color="red"),
                                                            margin="auto"
                                                        ),
                                                        rx.cond(
                                                        (UserState.user_rank >= 110) & (UserState.user_rank <= 118),
                                                            rx.vstack(
                                                                rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09114s02160s43114s44114s551146658334ce718b6a48aae7501ee31d755.png", width="85px", height="auto", margin="auto"),
                                                                rx.heading("JERARQUIA ANGELICAL", color="red"),
                                                                margin="auto"
                                                            ),
                                                            rx.cond(
                                                            (UserState.user_rank >= 119) & (UserState.user_rank <= 127),
                                                                rx.vstack(
                                                                    rx.image(src="https://www.habbo.es/habbo-imaging/badge/b27064s36117s43114s55101s41014acef07ff12b2c46af1b0a22ca8debe69.png", width="85px", height="auto", margin="auto"),
                                                                    rx.heading("CABALLERIA REAL", color="red"),
                                                                    margin="auto"
                                                                ),
                                                                rx.cond(
                                                                    (UserState.user_rank >= 128) & (UserState.user_rank <= 136),
                                                                    rx.vstack(
                                                                        rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09134s02230s01114s38014s55100350496d030029a7333ea1f71c0681567.png", width="85px", height="auto", margin="auto"),
                                                                        rx.heading("GENERALES", color="red"),
                                                                        margin="auto"
                                                                    ),
                                                                    rx.cond(
                                                                        (UserState.user_rank >= 137) & (UserState.user_rank <= 145),
                                                                        rx.vstack(
                                                                            rx.image(src="https://www.habbo.es/habbo-imaging/badge/b09014s36047s44114s43114s551007863875236acb89e543a87bab2231164.png", width="85px", height="auto", margin="auto"),
                                                                            rx.heading("DARK SIDER", color="red"),
                                                                            margin="auto"
                                                                        ),
                                                                        rx.cond(
                                                                            (UserState.user_rank >= 146) & (UserState.user_rank <= 152),
                                                                            rx.vstack(
                                                                                rx.image(src="https://www.habbo.es/habbo-imaging/badge/b17114s02137s36117s43104s2511459ba77acec4eefba49546e7c7afa60bf.png", width="85px", height="auto", margin="auto"),
                                                                                rx.heading("MITICOS", color="red"),
                                                                                margin="auto"
                                                                            ),
                                                                            rx.cond(
                                                                            (UserState.user_rank == 153),
                                                                                rx.vstack(
                                                                                    rx.image(src="https://www.habbo.es/habbo-imaging/badge/b22014s36014s36017t22014s55011c4a1a8a548c60bd6044ed4bc671a9d31.png", width="85px", height="auto", margin="auto"),
                                                                                    rx.heading("TITAN", color="red"),
                                                                                    margin="auto"
                                                                                ),
                                                                                rx.cond(
                                                                                    (UserState.user_rank == 154),
                                                                                        rx.vstack(
                                                                                            rx.image(src="https://www.habbo.es/habbo-imaging/badge/b17114s02137s36117s43104s2511459ba77acec4eefba49546e7c7afa60bf.png", width="85px", height="auto", margin="auto"),
                                                                                            rx.heading("SEMI DIOS", color="red"),
                                                                                            margin="auto"
                                                                                        ),
                                                                                        rx.cond(
                                                                                        (UserState.user_rank == 155),
                                                                                            rx.vstack(
                                                                                                rx.image(src="https://www.habbo.es/habbo-imaging/badge/b21114t47014t53117s25114s55100ae36bb064bed76f21adbddad94eeb74c.png", width="85px", height="auto", margin="auto"),
                                                                                                rx.heading("DIOS DE LA GUERRA", color="red"),
                                                                                                margin="auto"
                                                                                            ),
                                                                                            rx.cond(
                                                                                            (UserState.user_rank >= 156) & (UserState.user_rank <= 159),
                                                                                                rx.vstack(
                                                                                                    rx.image(src="https://www.habbo.es/habbo-imaging/badge/b27164s02114s36117s43114s55114138d8cb1eb289f409565bfcf2ed66f5b.png", width="85px", height="auto", margin="auto"),
                                                                                                    rx.heading("Dioses", color="red"),
                                                                                                    margin="auto"
                                                                                                ),
                                                                                            
                                                                                            ),
                                                                                        ),
                                                                                    ),
                                                                                    
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            rx.spacer(),
        border_radius="1em",
        border="4px solid",
        border_color=rx.color("red", 5),
        box_shadow=f"0 4px 6px {rx.color('red', 11)}",
        width="90%",
        height="auto")
    )
