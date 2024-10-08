USE [DB_MODULO]
GO
/****** Object:  Table [dbo].[documents]    Script Date: 5/09/2024 7:44:20 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[documents](
	[idDoc] [int] IDENTITY(1,1) NOT NULL,
	[nameDoc] [varchar](55) NULL,
	[pathDoc] [varchar](100) NULL,
	[enableDoc] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[idDoc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[documentsTemp]    Script Date: 5/09/2024 7:44:20 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[documentsTemp](
	[idDoc] [int] IDENTITY(1,1) NOT NULL,
	[nameDoc] [varchar](55) NULL,
	[pathDoc] [varchar](100) NULL,
	[enableDoc] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[idDoc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[typeUsers]    Script Date: 5/09/2024 7:44:20 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[typeUsers](
	[idtypeUser] [int] NOT NULL,
	[typeUser] [int] NULL,
	[rol] [varchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[idtypeUser] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[users]    Script Date: 5/09/2024 7:44:20 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[users](
	[idUser] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](50) NOT NULL,
	[lastname] [varchar](50) NOT NULL,
	[password] [nvarchar](255) NULL,
	[typeUserId] [int] NOT NULL,
	[username] [varchar](25) NULL,
	[mail] [varchar](255) NULL,
	[photo] [varchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[idUser] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[works]    Script Date: 5/09/2024 7:44:20 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[works](
	[idWork] [int] IDENTITY(1,1) NOT NULL,
	[lastname] [varchar](50) NOT NULL,
	[idUserTec] [int] NOT NULL,
	[idUserSup] [int] NOT NULL,
	[nameDoc] [varchar](55) NULL,
	[pathDoc] [varchar](100) NULL,
	[enableWork] [bit] NULL,
	[checkSup] [bit] NULL,
	[workDone] [bit] NULL,
	[typeWork] [varchar](25) NULL,
	[ubicacion] [varchar](25) NULL,
	[dateWork] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[idWork] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[users]  WITH CHECK ADD  CONSTRAINT [FK_typeUser_typeUserId] FOREIGN KEY([typeUserId])
REFERENCES [dbo].[typeUsers] ([idtypeUser])
GO
ALTER TABLE [dbo].[users] CHECK CONSTRAINT [FK_typeUser_typeUserId]
GO
ALTER TABLE [dbo].[works]  WITH CHECK ADD FOREIGN KEY([idUserSup])
REFERENCES [dbo].[users] ([idUser])
GO
