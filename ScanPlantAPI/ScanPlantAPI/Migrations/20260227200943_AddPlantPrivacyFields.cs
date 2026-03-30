using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ScanPlantAPI.Migrations
{
    /// <inheritdoc />
    public partial class AddPlantPrivacyFields : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<bool>(
                name: "IsInCommunity",
                table: "Plants",
                type: "boolean",
                nullable: false,
                defaultValue: false);

            migrationBuilder.AddColumn<bool>(
                name: "IsLocationPublic",
                table: "Plants",
                type: "boolean",
                nullable: false,
                defaultValue: false);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "IsInCommunity",
                table: "Plants");

            migrationBuilder.DropColumn(
                name: "IsLocationPublic",
                table: "Plants");
        }
    }
}
